import json
import random
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from django.core import serializers
from .serializers import *
from authentication.device_auth import auth_required

class Albums(APIView):
  parser_classes = (parsers.MultiPartParser, parsers.FormParser,) 
  serializer_class = AlbumSerializer


  def get(self, request,device_auth,format=None):
    if auth_required(device_auth) == True:
      albums = Albums.objects.all()
      if not albums:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      albums_serializer = AlbumSerializer(albums, many=True,context={'device_key': device_auth}
).data
      return Response(albums_serializer, status=status.HTTP_200_OK)
    else:
      return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)
  
