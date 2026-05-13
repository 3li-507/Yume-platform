from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/view/', views.contact_view_all, name='contact_view_all'),
    path('contact/view/<int:contact_id>/', views.contact_view_detail, name='contact_view_detail'),
    path('services/', views.services_view, name='services_view'),
    path('cities/', views.cities_view, name='cities_view'),
    path('mode/<mode>/', views.mode_view, name='mode_view'),
]
