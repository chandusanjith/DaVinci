from django.urls import path, include


urlpatterns = [
    path('CheckAstrology/<device_auth>/', Horoscope.as_view(), name='check_horoscope')
]
