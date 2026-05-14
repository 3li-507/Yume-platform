from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import City, CapsuleHotel, Capsule
from .forms import CapsuleHotelForm, CapsuleForm
from django.core.paginator import Paginator

# ── City Views ──

# Admin
def city_list(request):
    cities = City.objects.all()
    return render(request, 'hotels/city_list.html', {'cities': cities})


# ── CapsuleHotel Views ──

# Customer, Guest
def hotel_list(request):
    hotels = CapsuleHotel.objects.filter(is_active=True)

    # ── Search ──
    q = request.GET.get('q')
    if q:
        hotels = hotels.filter(name__icontains=q)

    # ── City Filter ──
    city_id = request.GET.get('city')
    if city_id:
        hotels = hotels.filter(city__id=city_id)

    # ── Booking Type Filter ──
    booking_type = request.GET.get('booking_type')
    if booking_type == 'hour':
        hotels = hotels.filter(capsules__hour_price__isnull=False).distinct()
    elif booking_type == 'night':
        hotels = hotels.filter(capsules__night_price__isnull=False).distinct()

    # ── Price Filter ──
    price = request.GET.get('price')
    if price == 'low':
        hotels = hotels.filter(capsules__hour_price__lt=100).distinct()
    elif price == 'mid':
        hotels = hotels.filter(capsules__hour_price__range=(100, 300)).distinct()
    elif price == 'high':
        hotels = hotels.filter(capsules__hour_price__gt=300).distinct()

    # ── Pagination ──
    paginator = Paginator(hotels, 6)  # 6 hotels per page
    page_number = request.GET.get('page')
    hotels = paginator.get_page(page_number)

    cities = City.objects.filter(is_active=True)

    return render(request, 'hotels/hotel_list.html', {
        'hotels': hotels,
        'cities': cities,
    })
# def hotel_list(request):
#     hotels = CapsuleHotel.objects.filter(is_active=True)
#     return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

# Customer, Guest
def hotel_detail(request, pk):
    hotel = get_object_or_404(CapsuleHotel, pk=pk)
    capsules = hotel.capsules.filter(is_available=True)
    reviews = hotel.review_set.all().order_by('-created_at')[:5]
    related_hotels = CapsuleHotel.objects.filter(
        city=hotel.city,
        is_active=True
    ).exclude(pk=pk)[:3]

    return render(request, 'hotels/hotel_detail.html', {
        'hotel': hotel,
        'capsules': capsules,
        'reviews': reviews,
        'related_hotels': related_hotels,
    })


# Hotel Owner
def hotel_create(request):
    if request.method == 'POST':
        form = CapsuleHotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.hotel_owner = request.user.ownerprofile
            hotel.is_active = False  # waiting for admin approval
            hotel.save()
            return redirect('hotels:hotel_list')
    else:
        form = CapsuleHotelForm()
    return render(request, 'hotels/hotel_form.html', {'form': form})

# Hotel Owner
def hotel_update(request, pk):
    hotel = get_object_or_404(CapsuleHotel, pk=pk)
    if request.method == 'POST':
        form = CapsuleHotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotels:hotel_detail', pk=pk)
    else:
        form = CapsuleHotelForm(instance=hotel)
    return render(request, 'hotels/hotel_form.html', {'form': form})

# Hotel Owner
def hotel_delete(request, pk):
    hotel = get_object_or_404(CapsuleHotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotels:hotel_list')
    return render(request, 'hotels/hotel_confirm_delete.html', {'hotel': hotel})


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
    hotel = get_object_or_404(CapsuleHotel, pk=hotel_pk)
    if request.method == 'POST':
        form = CapsuleForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['capsule_count']
            for i in range(1, count + 1):
                Capsule.objects.create(
                    hotel=hotel,
                    capsule_num=f"{hotel.id}-{i}",
                    hour_price=form.cleaned_data['hour_price'],
                    night_price=form.cleaned_data['night_price'],
                )
            return redirect('hotels:capsule_list', hotel_pk=hotel_pk)
    else:
        form = CapsuleForm()
    return render(request, 'hotels/capsule_form.html', {
        'form': form,
        'hotel': hotel
    })


# Hotel Owner
def capsule_update(request, pk):
    capsule = get_object_or_404(Capsule, pk=pk)
    if request.method == 'POST':
        form = CapsuleForm(request.POST, instance=capsule)
        if form.is_valid():
            form.save()
            return redirect('hotels:capsule_list', hotel_pk=capsule.hotel.pk)
    else:
        form = CapsuleForm(instance=capsule)
    return render(request, 'hotels/capsule_form.html', {
        'form': form,
        'hotel': capsule.hotel
    })


# Hotel Owner
def capsule_delete(request, pk):
    capsule = get_object_or_404(Capsule, pk=pk)
    hotel_pk = capsule.hotel.pk
    if request.method == 'POST':
        capsule.delete()
        return redirect('hotels:capsule_list', hotel_pk=hotel_pk)
    return render(request, 'hotels/capsule_confirm_delete.html', {'capsule': capsule})