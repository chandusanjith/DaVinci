from rest_framework import serializers

from authentication.models import DeviceAuth
from .models import *

class DeviceAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAuth
        fields = '__all__'

class DeviceLoginLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLoginLog
        fields = '__all__'