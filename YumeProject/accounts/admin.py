from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, OwnerProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Yume Role & Profile', {
            'fields': ('role', 'profile_image'),
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Yume Role & Profile', {
            'fields': ('role', 'profile_image'),
        }),
    )
    list_display  = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter   = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'company_name', 'company_id', 'company_location')
    search_fields = ('user__username', 'user__email', 'company_name', 'company_id')
