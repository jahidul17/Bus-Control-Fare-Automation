from django.db import models
from django.utils import timezone

class Passenger(models.Model):
    name = models.CharField(max_length=120)
    eid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.0)
    is_onboard = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TripTransaction(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    boarding_time = models.DateTimeField(null=True, blank=True)
    boarding_location = models.CharField(max_length=120, null=True, blank=True)
    alight_time = models.DateTimeField(null=True, blank=True)
    alight_location = models.CharField(max_length=120, null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    fare = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    paid = models.BooleanField(default=False)


