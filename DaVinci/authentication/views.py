import json
import random
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from django.core import serializers

from .models import *
from .serializers import *

from datetime import date

class DeviceLogin(APIView):

  def get(self, request, device_auth,format=None):
     if len(device_auth) != 16:
       return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)
     if DeviceAuth.objects.filter(device_key=device_auth).exists():
        app_version = AppParameters.objects.filter(parameter_name="APP_VERSION").first()
        app_force_update = AppParameters.objects.filter(parameter_name="FORCE_UPDATE").first()
        mapped_key = DeviceAuth.objects.filter(device_key = device_auth).first()
        return Response({"Auth_key":mapped_key.mapped_key,
                        "app_version":app_version.parameter_value,
                        "app_force_update":app_force_update.parameter_value,
                        "user_type_old":"OLD_USER"}, status=status.HTTP_200_OK)
     else:
         mapped_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
         new_data = DeviceAuth(device_key=device_auth, mapped_key=mapped_id)
         new_data.save()
         app_version = AppParameters.objects.filter(parameter_name="APP_VERSION").first()
         app_force_update = AppParameters.objects.filter(parameter_name="FORCE_UPDATE").first()
         mapped_key = DeviceAuth.objects.filter(device_key = device_auth).first()
         return Response({"Auth_key":mapped_key.mapped_key,
                        "app_version":app_version.parameter_value,
                        "app_force_update":app_force_update.parameter_value,
                        "user_type_new":"NEW_USER"}, status=status.HTTP_200_OK)