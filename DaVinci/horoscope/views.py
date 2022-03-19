import json
import random
import string

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from django.shortcuts import render
from django.views.generic import View

from language_translator.views import _translate
from .astrology import horoscope_info
from .serializers import HoroscopeUsersLogSerializer
from authentication.device_auth import auth_required
from django.core import serializers
from .models import HoroscopeUsersLog

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

days = [
    'today', 'tomorrow', 'yesterday'
]

languages = [
  'kn', 'default', 'en'
]

class Horoscope(APIView):
  serializer_class = HoroscopeUsersLogSerializer

  def get_serializer_class(self):
    return self.serializer_class

  def post(self, request, device_auth, format=None):
    if auth_required(device_auth) == True:
      print(request.data['nameValuePairs']['device'])
      sign = request.data['nameValuePairs']['sign'].lower()
      day = request.data['nameValuePairs']['day'].lower()
      timezone = request.data['nameValuePairs']['timezone']
      language = request.data['nameValuePairs']['language']
      try:
          if language not in languages:
             return Response({"ERROR":"Improper Language"}, status=status.HTTP_404_NOT_FOUND)
          if (sign not in signs) or (day not in days):
              return Response({"ERROR":"Improper sign or day"}, status=status.HTTP_404_NOT_FOUND)
          response = horoscope_info(sign=sign, day=day, tz=timezone)
          if language == "kn":
            tranlated_response = _translate(response, language)
          elif language == "default":
            resp_context = {}
            resp_context['english']=response
            response = _translate(response, "kn")
            resp_context['kannada']= response
            tranlated_response = resp_context
          else:
            tranlated_response = response

          log = HoroscopeUsersLog(device_key =device_auth, day = day, sign=sign, timezone=timezone, language=language, out_message =tranlated_response)
          log.save()
          return Response(tranlated_response, status=status.HTTP_200_OK)
      except Exception as e:
          log = HoroscopeUsersLog(device_key =device_auth, day = day, sign=sign, timezone=timezone, language=language, out_message =e)
          log.save()
          return Response({"ERROR":"OOps! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)
    else:
      return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)

class GetHoroscopeLog(APIView):
  def get(self, request,format=None):
    try:
      horoscope_log = HoroscopeUsersLog.objects.all()
      if not horoscope_log:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      horoscope_log_serializer = HoroscopeUsersLogSerializer(horoscope_log, many=True
).data
      return Response(horoscope_log_serializer, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({
          "ERROR":"OOps!! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)

class HoroscopeWeb(View):
  def get(self, *args, **kwargs):
    if auth_required(kwargs['device_auth']) == True:
      device_auth = kwargs['device_auth']
      sign = kwargs['sign'].lower()
      day = kwargs['day'].lower()
      timezone = 'Asia/Kolkata'
      language = kwargs['language']
      try:
          if language not in languages:
             return render(self.request, 'horoscope.html', {"MESSAGE":"Improper Language"})
          if (sign not in signs) or (day not in days):
              return render(self.request, 'horoscope.html', {"MESSAGE":"Improper sign or day"})
          response = horoscope_info(sign=sign, day=day, tz=timezone)
          if language == "kn":
            resp_context = {}
            tranlated_response = _translate(response, language)
            resp_context['kannada'] = tranlated_response
          elif language == "default":
            resp_context = {}
            resp_context['english']=response
            response = _translate(response, "kn")
            resp_context['kannada']= response
          else:
            resp_context = {}
            resp_context['english'] = response

          log = HoroscopeUsersLog(device_key =device_auth, day = day, sign=sign, timezone=timezone, language=language, out_message =resp_context)
          log.save()
          return render(self.request, 'horoscope.html', resp_context)
      except Exception as e:
          log = HoroscopeUsersLog(device_key =device_auth, day = day, sign=sign, timezone=timezone, language=language, out_message =e)
          log.save()
          return render(self.request, 'horoscope.html', {"MESSAGE":"OOps! something went wrong!!"})
    else:
        return render(self.request, 'horoscope.html', {"MESSAGE":"Access Denied"})
