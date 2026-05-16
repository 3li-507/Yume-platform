from django import forms
from hotels.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'is_active']
