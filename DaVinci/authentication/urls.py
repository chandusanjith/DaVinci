from django.urls import path, include

from .views import DeviceLogin


urlpatterns = [
    path('DeviceLogin/<device_auth>/', DeviceLogin.as_view(), name='device_login')
]
