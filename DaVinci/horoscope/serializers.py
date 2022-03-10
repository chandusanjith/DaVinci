from rest_framework import serializers

from .models import *

class HoroscopeUsersLogSerializer(serializers.ModelSerializer):
   class Meta:
        model = HoroscopeUsersLog
        fields = '__all__'