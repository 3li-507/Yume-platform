from django import forms
from hotels.models import CapsuleHotel, Capsule, City


class CapsuleHotelForm(forms.ModelForm):
    class Meta:
        model = CapsuleHotel
        fields = ['name', 'description', 'address', 'image', 'city']


class CapsuleForm(forms.ModelForm):
    capsule_count = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = Capsule
        fields = ['hour_price', 'night_price']