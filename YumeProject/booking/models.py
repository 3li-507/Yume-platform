from django.db import models
from accounts.models import CustomerProfile
from hotels.models import Capsule

class Booking(models.Model):
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    booking_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')

    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='bookings')
    capsule = models.ForeignKey(Capsule, on_delete=models.CASCADE, related_name='bookings')