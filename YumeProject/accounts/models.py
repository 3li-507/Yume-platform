from django.contrib.auth.models import AbstractUser
from django.db import models

GROUP_GUEST = 1
GROUP_OWNER = 2
GROUP_ADMIN = 3

ROLE_CHOICES = [
    (GROUP_GUEST, 'Guest'),
    (GROUP_OWNER, 'Owner'),
    (GROUP_ADMIN, 'Admin'),
]


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=GROUP_GUEST)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    @property
    def is_guest(self):
        return self.role == GROUP_GUEST

    @property
    def is_owner(self):
        return self.role == GROUP_OWNER

    @property
    def is_admin_role(self):
        return self.role == GROUP_ADMIN

    def __str__(self):
        role_label = dict(ROLE_CHOICES).get(self.role, 'Unknown')
        return f"{self.username} ({role_label})"


class OwnerProfile(models.Model):
    user             = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='owner_profile')
    company_name     = models.CharField(max_length=200)
    company_id       = models.CharField(max_length=100)
    company_location = models.CharField(max_length=200)

    def __str__(self):
        return f"OwnerProfile({self.user.username} — {self.company_name})"
