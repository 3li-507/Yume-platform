from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomerSignUpForm, OwnerSignUpForm, SignInForm
from .models import CustomerProfile, OwnerProfile, GROUP_CUSTOMER, GROUP_OWNER


def sign_up(request):
    return redirect('accounts:sign_up_guest')


def sign_up_guest(request):
    if request.user.is_authenticated:
        return redirect('main:home_view')

    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = GROUP_CUSTOMER
            user.save()
            CustomerProfile.objects.create(
                user=user,
                avatar=form.cleaned_data.get('avatar'),
            )
            login(request, user)
            return redirect('main:home_view')
    else:
        form = CustomerSignUpForm()

    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_up_owner(request):
    if request.user.is_authenticated:
        return redirect('main:home_view')

    if request.method == 'POST':
        form = OwnerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = GROUP_OWNER
            user.save()
            OwnerProfile.objects.create(
                user=user,
                company_name=form.cleaned_data['company_name'],
                commercial_reg=form.cleaned_data['commercial_reg'],
                avatar=form.cleaned_data.get('avatar'),
            )
            login(request, user)
            return redirect('main:home_view')
    else:
        form = OwnerSignUpForm()

    return render(request, 'accounts/sign_up_company.html', {'form': form})

#TODO:
def edit_profile(request):
    if request.method == 'POST':
        pass

def company_profile_view(request):
    return render(request, 'accounts/company_profile.html',)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('main:home_view')

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'main:home_view')
                return redirect(next_url)
            messages.error(request, 'Invalid username or password.')
    else:
        form = SignInForm()

    return render(request, 'accounts/sign_in.html', {'form': form})


@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
    return redirect('main:home_view')


@login_required
def account_view(request):
    return render(request, 'accounts/account.html')
