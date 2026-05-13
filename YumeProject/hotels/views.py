from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import City, CapsuleHotel, Capsule

def hotels_view(request):
    return request(200)



# ── City Views ──
def city_list(request):
    pass


# ── CapsuleHotel Views ──
def hotel_list(request):
    pass

def hotel_detail(request, pk):
    pass

def hotel_create(request):
    pass

def hotel_update(request, pk):
    pass

def hotel_delete(request, pk):
    pass


# ── Capsule Views ──
def capsule_list(request, hotel_pk):
    pass

def capsule_create(request, hotel_pk):
    pass

def capsule_update(request, pk):
    pass

def capsule_delete(request, pk):
    pass
