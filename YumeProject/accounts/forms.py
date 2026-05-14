from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator



phone_validator = RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')

User = get_user_model()


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name  = forms.CharField(max_length=150, required=True)
    email      = forms.EmailField(required=True)
    avatar     = forms.ImageField(required=False)
    phone_number      = forms.CharField(required=True,validators=[phone_validator])
   

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class OwnerSignUpForm(UserCreationForm):
    first_name   = forms.CharField(max_length=150, required=True)
    last_name    = forms.CharField(max_length=150, required=True)
    email        = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=200)
    commercial_reg = forms.CharField(max_length=100)
    avatar       = forms.ImageField(required=False)
    phone_number = forms.CharField(required=True,validators=[phone_validator])

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
