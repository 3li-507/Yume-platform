
from django.urls import path, include
from . import views

app_name="hotelOwner"

urlpatterns = [
    path('', views.owner_view, name='owner_view'),
    
]