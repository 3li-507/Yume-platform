from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('services/', views.services_view, name='services_view'),
    path('cities/', views.Cities_view, name='Cities_view'),
    path('mode/<mode>/', views.mode_view, name='mode_view'),
]
