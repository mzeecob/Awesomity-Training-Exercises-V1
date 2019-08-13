from .models import *
from django import forms


class coordinates(forms.ModelForm):
    location_name = forms.CharField(label='Location name')
    coordinates = forms.CharField()

    class Meta:
        model = Coordinates
        fields = ['location_name', 'coordinates']



