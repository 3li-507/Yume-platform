from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

from .models import GROUP_OWNER, GROUP_ADMIN


def owner_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f'/accounts/sign-in/?next={request.path}')
        if request.user.role not in (GROUP_OWNER, GROUP_ADMIN):
            messages.error(request, 'Owner access required.')
            return redirect('main:home_view')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_role_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f'/accounts/sign-in/?next={request.path}')
        if request.user.role != GROUP_ADMIN:
            messages.error(request, 'Admin access required.')
            return redirect('main:home_view')
        return view_func(request, *args, **kwargs)
    return wrapper
