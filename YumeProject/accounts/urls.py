from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',          views.account_view, name='account_view'),
    path('sign-up/',  views.sign_up,      name='sign_up'),
    path('sign-in/',  views.sign_in,      name='sign_in'),
    path('sign-out/', views.sign_out,     name='sign_out'),
]
