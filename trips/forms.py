from django import forms
from .models import Passenger

LOCATIONS = [
    ("Badda", "Badda"),
    ("Jatrabari", "Jatrabari"),
    ("Gulshan", "Gulshan"),
]

class ScanForm(forms.Form):
    passenger = forms.ModelChoiceField(queryset=Passenger.objects.all())
    location = forms.ChoiceField(choices=LOCATIONS)
    action = forms.ChoiceField(choices=[("board", "Board"), ("alight", "Alight")])


