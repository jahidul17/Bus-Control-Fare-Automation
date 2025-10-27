from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Passenger, TripTransaction
from .forms import ScanForm
from .utils import haversine_km, fare_calc, loc_coords
from decimal import Decimal


def home(request):
    passengers = Passenger.objects.all()
    trips = TripTransaction.objects.all().order_by('-boarding_time')
    form = ScanForm(request.POST or None)
    message = ""
    
    if request.method == "POST" and form.is_valid():
        passenger = form.cleaned_data['passenger']
        location = form.cleaned_data['location']
        action = form.cleaned_data['action']
        
        if action == "board":
            if passenger.is_onboard:
                message = f"{passenger.name} is already onboard!"
            else:
                passenger.is_onboard = True
                passenger.save()
                TripTransaction.objects.create(
                    passenger=passenger,
                    boarding_time=timezone.now(),
                    boarding_location=location
                )
                message = f"{passenger.name} boarded at {location}."
        
        elif action == "alight":
            if not passenger.is_onboard:
                message = f"{passenger.name} is not onboard!"
            else:
                trip = TripTransaction.objects.filter(passenger=passenger, alight_time__isnull=True).last()
                lat1, lon1 = loc_coords.get(trip.boarding_location, (0,0))
                lat2, lon2 = loc_coords.get(location, (0,0))
                distance = haversine_km(lat1, lon1, lat2, lon2)
                fare = fare_calc(distance)
                                
                passenger.balance -= Decimal(fare)
                passenger.is_onboard = False
                passenger.save()

                trip.alight_time = timezone.now()
                trip.alight_location = location
                trip.distance_km = distance
                trip.fare = fare
                trip.paid = True
                trip.save()
                
                message = f"{passenger.name} alighted at {location}. Distance: {distance:.2f} km, Fare: {fare:.2f}"
        
        return redirect("home")
    
    return render(request, "trips/home.html", {"passengers": passengers, "trips": trips, "form": form, "message": message})

