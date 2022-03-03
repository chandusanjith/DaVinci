import json
import random
import string

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from .astrology import horoscope_info
from .serializers import HoroscopeSerializer
from django.core import serializers

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

days = [
    'today', 'tomorrow', 'yesterday'
]


class Horoscope(APIView):
  serializer_class = HoroscopeSerializer

  def get_serializer_class(self):
    return self.serializer_class
  
  def post(self, request, device_auth, format=None):
    
    sign = request.data['sign'].lower()
    day = request.data['day'].lower()
    timezone = request.data['timezone']
    try:
        if (sign not in signs) or (day not in days):
            return Response({"ERROR":"Improper sign or day"}, status=status.HTTP_404_NOT_FOUND)
        response = horoscope_info(sign=sign, day=day, tz=timezone)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"ERROR":"OOps! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)