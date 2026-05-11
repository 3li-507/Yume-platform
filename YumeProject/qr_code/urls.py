from django.urls import path
from . import views

app_name = 'qr_code'

urlpatterns = [
    path('/qr', views.qr_code, name='qr_code'),
]
