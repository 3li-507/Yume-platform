from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.account_view, name='account_view'),
]
