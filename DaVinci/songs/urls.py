from django.urls import path, include

from .views import *

urlpatterns = [
    path('Albums/<device_auth>/', Albums.as_view(), name='get_albums')
]