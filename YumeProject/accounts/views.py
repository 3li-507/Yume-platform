from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomerSignUpForm, OwnerSignUpForm, SignInForm
from .models import CustomerProfile, OwnerProfile, GROUP_CUSTOMER, GROUP_OWNER


def sign_up(request):
    account_type = request.POST.get('account_type', request.GET.get('type', 'customer'))
    is_owner = (account_type == 'owner')
    FormClass = OwnerSignUpForm if is_owner else CustomerSignUpForm

    if request.user.is_authenticated:
        return redirect('main:home_view')

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = GROUP_OWNER if is_owner else GROUP_CUSTOMER
            user.save()
            if is_owner:
                OwnerProfile.objects.create(
                    user=user,
                    company_name=form.cleaned_data['company_name'],
                    company_id=form.cleaned_data['company_id'],
                    avatar=form.cleaned_data.get('avatar'),
                )
            else:
                CustomerProfile.objects.create(
                    user=user,
                    avatar=form.cleaned_data.get('avatar'),
                )
            login(request, user)
            return redirect('main:home_view')
    else:
        form = FormClass()

    return render(request, 'accounts/sign_up.html', {
        'form': form,
        'is_owner': is_owner,
        'account_type': account_type,
    })


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
