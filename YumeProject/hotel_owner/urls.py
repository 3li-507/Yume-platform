
from django.urls import path, include
from . import views

app_name="hotel_owner"

urlpatterns = [
    path('', views.owner_view, name='owner_view'),
    
]