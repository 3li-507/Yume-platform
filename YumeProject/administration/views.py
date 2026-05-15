from django.http import HttpResponse
from accounts.decorators import admin_role_required
from django.shortcuts import render
from hotels.models import CapsuleHotel, Capsule

# Create your views here.


@admin_role_required
def admin_view(request):
    context ={
        #'pending_hotels': CapsuleHotel.objects.filter(status=CapsuleHotel.STATUS_PENDING).select_related('hotel_owner__user', 'city'),
#        'approved_hotels': CapsuleHotel.objects.filter(status=CapsuleHotel.STATUS_APPROVED).select_related('hotel_owner__user', 'city'),

        'pending_hotels': CapsuleHotel.objects.select_related('hotel_owner__user', 'city'),
        

    }
    return render(request, 'administration/dashboard.html')


