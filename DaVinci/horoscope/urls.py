from django.urls import path, include

from .views import *

urlpatterns = [
    path('CheckAstrology/<device_auth>/', Horoscope.as_view(), name='check_horoscope'),
    path('GetHoroscopeLog/', GetHoroscopeLog.as_view(), name='get_horoscope_log'),
    path('CheckAstrologyWeb/<sign>/<day>/<language>/<device_auth>/', HoroscopeWeb.as_view(), name='check_horoscope_web'),
]
