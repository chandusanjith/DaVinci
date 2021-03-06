import json
import random
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from django.core import serializers

from .models import *
from .serializers import DeviceAuthSerializer,DeviceLoginLogSerializer

from datetime import date

class DeviceLogin(APIView):
  
  def storeLoginDetails(self, device_key_ui):
    device_instance = DeviceAuth.objects.filter(device_key=device_key_ui).first()
    if DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).exists():
        data = DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).first()
        DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).update(logged_count=data.logged_count + 1)
    else:
        DeviceLoginLog.objects.create(device=device_instance, logged_count=1)

  def get(self, request, device_auth,format=None):
     if len(device_auth) != 16:
       return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)
     if DeviceAuth.objects.filter(device_key=device_auth).exists():
        app_version = AppParameters.objects.filter(parameter_name="APP_VERSION").first()
        app_force_update = AppParameters.objects.filter(parameter_name="FORCE_UPDATE").first()
        mapped_key = DeviceAuth.objects.filter(device_key = device_auth).first()
        self.storeLoginDetails(device_auth)
        return Response({"auth_key":mapped_key.mapped_key,
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
         self.storeLoginDetails(device_auth)
         return Response({"auth_key":mapped_key.mapped_key,
                        "app_version":app_version.parameter_value,
                        "app_force_update":app_force_update.parameter_value,
                        "user_type_new":"NEW_USER"}, status=status.HTTP_200_OK)

class DeviceMappingsView(APIView):
  serializer_class = DeviceAuthSerializer

  def get(self, request,format=None):
    try:
      device_mapping_details = DeviceAuth.objects.all()
      if not device_mapping_details:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      device_mapping_serializer = DeviceAuthSerializer(device_mapping_details, many=True
).data
      return Response(device_mapping_serializer, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({
          "ERROR":"OOps!! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)

class DeviceActivityView(APIView):
  serializer_class = DeviceLoginLogSerializer

  def get(self, request,format=None):
    try:
      device_login_details = DeviceLoginLog.objects.all()
      if not device_login_details:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      device_login_serializer = DeviceLoginLogSerializer(device_login_details, many=True
).data
      return Response(device_login_serializer, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({
          "ERROR":"OOps!! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)