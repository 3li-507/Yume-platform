from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('',                          views.admin_view,   name='admin_view'),
    path('hotels/<int:hotel_id>/toggle/', views.toggle_hotel, name='toggle_hotel'),
    path('cities/add/',                   views.add_city,     name='add_city'),
]
