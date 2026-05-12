from django.contrib.auth.models import AbstractUser
from django.db import models

GROUP_CUSTOMER = 1
GROUP_OWNER = 2
GROUP_ADMIN = 3

ROLE_CHOICES = [
    (GROUP_CUSTOMER, 'Customer'),
    (GROUP_OWNER, 'Owner'),
    (GROUP_ADMIN, 'Admin'),
]


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=GROUP_CUSTOMER)

    @property
    def is_customer(self):
        return self.role == GROUP_CUSTOMER

    @property
    def is_owner(self):
        return self.role == GROUP_OWNER

    @property
    def is_admin_role(self):
        return self.role == GROUP_ADMIN

    def __str__(self):
        role_label = dict(ROLE_CHOICES).get(self.role, 'Unknown')
        return f"{self.username} ({role_label})"


class CustomerProfile(models.Model):
    user   = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='customer_profile')
    avatar = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"CustomerProfile({self.user.username})"


class OwnerProfile(models.Model):
    user         = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='owner_profile')
    company_name = models.CharField(max_length=200)
    company_id   = models.CharField(max_length=100)
    avatar       = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"OwnerProfile({self.user.username} — {self.company_name})"
