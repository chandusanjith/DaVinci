from django.urls import path, include

from .views import *

urlpatterns = [
    path('AddFeedback/', AddFeedbackView.as_view(), name='add_feedback'),
    path('GetFeedback/<device_id>/', GetFeedbackView.as_view(), name='get_feedback'),
]