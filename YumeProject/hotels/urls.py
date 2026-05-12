from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    # path('', views.hotels_view, name='hotels_view'),
    # ── City ──
    path('cities/', views.city_list, name='city_list'),

    # ── CapsuleHotel ──
    path('', views.hotel_list, name='hotel_list'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('create/', views.hotel_create, name='hotel_create'),
    path('<int:pk>/update/', views.hotel_update, name='hotel_update'),
    path('<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),

    # ── Capsule ──
    path('<int:hotel_pk>/capsules/', views.capsule_list, name='capsule_list'),
    path('<int:hotel_pk>/capsules/create/', views.capsule_create, name='capsule_create'),
    path('capsules/<int:pk>/update/', views.capsule_update, name='capsule_update'),
    path('capsules/<int:pk>/delete/', views.capsule_delete, name='capsule_delete'),

]