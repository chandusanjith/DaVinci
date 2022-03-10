from rest_framework import serializers

from authentication.models import DeviceAuth
from .models import *

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'