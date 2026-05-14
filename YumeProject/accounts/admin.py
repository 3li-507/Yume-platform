from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, CustomerProfile, OwnerProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Yume Role', {
            'fields': ('role',),
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Yume Role', {
            'fields': ('role',),
        }),
    )
    list_display  = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter   = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'avatar')
    search_fields = ('user__username', 'user__email')


@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'company_name', 'commercial_reg', 'avatar')
    search_fields = ('user__username', 'user__email', 'company_name', 'commercial_reg')
