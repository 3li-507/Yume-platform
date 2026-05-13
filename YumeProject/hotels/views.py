from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import City, CapsuleHotel, Capsule

# ── City Views ──

# Admin
def city_list(request):
    cities = City.objects.all()
    return render(request, 'hotels/city_list.html', {'cities': cities})


# ── CapsuleHotel Views ──

# Customer, Guest
def hotel_list(request):
    hotels = CapsuleHotel.objects.filter(is_active=True)
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

# Customer, Guest
def hotel_detail(request, pk):
    hotel = CapsuleHotel.objects.get(pk=pk)
    capsules = hotel.capsules.filter(is_available=True)
    return render(request, 'hotels/hotel_detail.html', {
        'hotel': hotel,
        'capsules': capsules
    })

# Hotel Owner
def hotel_create(request):
    pass

# Hotel Owner
def hotel_update(request, pk):
    pass

# Hotel Owner
def hotel_delete(request, pk):
    pass


# ── Capsule Views ──

# Hotel Owner
def capsule_list(request, hotel_pk):
    hotel = CapsuleHotel.objects.get(pk=hotel_pk)
    capsules = hotel.capsules.all()
    return render(request, 'hotels/capsule_list.html', {
        'hotel': hotel,
        'capsules': capsules
    })

# Hotel Owner
def capsule_create(request, hotel_pk):
    pass

# Hotel Owner
def capsule_update(request, pk):
    pass

# Hotel Owner
def capsule_delete(request, pk):
    pass