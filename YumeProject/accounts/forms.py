from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class GuestSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name  = forms.CharField(max_length=150, required=True)
    email      = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_image']


class OwnerSignUpForm(UserCreationForm):
    first_name       = forms.CharField(max_length=150, required=True)
    last_name        = forms.CharField(max_length=150, required=True)
    email            = forms.EmailField(required=True)
    company_name     = forms.CharField(max_length=200)
    company_id       = forms.CharField(max_length=100)
    company_location = forms.CharField(max_length=200)

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_image']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
