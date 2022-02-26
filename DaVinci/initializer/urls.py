from django.urls import path, include

from .views import *

urlpatterns = [
    path('PrivacyPolicy/', privacy_policy, name='get_privacy_policy'),
    path('AboutUs/', about_us, name='get_about_us'),
    path('Terms/', terms, name='get_terms'),
]