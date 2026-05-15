from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    # path('', views.hotels_view, name='hotels_view'),
    path('', views.hotel_list, name='hotel_list'),
    path('cities/', views.city_list, name='city_list'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),

]