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
from .models import *


class MantraAlbumView(APIView):
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
    )
    serializer_class = MantraAlbumSerializer

    def get(self, request, device_auth, format=None):
        if auth_required(device_auth) == True:
            mantra_albums = MantraAlbum.objects.all()
            if not mantra_albums:
                return Response({"ERROR": "404 NO DATA FOUND :("},
                                status=status.HTTP_404_NOT_FOUND)
            albums_serializer = MantraAlbumSerializer(mantra_albums,
                                                      many=True,
                                                      context={
                                                          'device_key':
                                                          device_auth
                                                      }).data
            return Response(albums_serializer, status=status.HTTP_200_OK)
        else:
            return Response({"ERROR": "Access Denied"},
                            status=status.HTTP_404_NOT_FOUND)


class MantraView(APIView):
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
    )
    serializer_class = MantraSerializer

    def get(self, request, album_id, device_auth, format=None):
        if auth_required(device_auth) == True:
            mantra_album = MantraAlbum.objects.get(id=album_id)
            mantras = Mantra.objects.filter(album=mantra_album)
            if not mantras:
                return Response({"ERROR": "404 NO DATA FOUND :("},
                                status=status.HTTP_404_NOT_FOUND)
            mantra_serializer = MantraSerializer(mantras,
                                                 many=True,
                                                 context={
                                                     'device_key': device_auth
                                                 }).data
            return Response(mantra_serializer, status=status.HTTP_200_OK)
        else:
            return Response({"ERROR": "Access Denied"},
                            status=status.HTTP_404_NOT_FOUND)


class MantraLyricsView(APIView):
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
    )
    serializer_class = MantraLyricsSerializer

    def get(self, request, album_id, device_auth, format=None):
        if auth_required(device_auth) == True:
            mantra_album = MantraAlbum.objects.get(id=album_id)
            mantra_lyrics = MantraLyric.objects.filter(album=mantra_album)
            if not mantra_lyrics:
                return Response({"ERROR": "404 NO DATA FOUND :("},
                                status=status.HTTP_404_NOT_FOUND)
            mantra_lyrics_serializer = MantraLyricsSerializer(mantra_lyrics,
                                                              many=True,
                                                              context={
                                                                  'device_key':
                                                                  device_auth
                                                              }).data
            return Response(mantra_lyrics_serializer,
                            status=status.HTTP_200_OK)
        else:
            return Response({"ERROR": "Access Denied"},
                            status=status.HTTP_404_NOT_FOUND)
