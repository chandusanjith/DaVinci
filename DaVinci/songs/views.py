import json
import random
import string
import os

from threading import Thread
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers

from django.core import serializers
from .serializers import *
from authentication.device_auth import auth_required
from .models import *

class AlbumsView(APIView):
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

class LyricsAlbumView(APIView):
  parser_classes = (parsers.MultiPartParser, parsers.FormParser,) 
  serializer_class = LyricsAlbumSerializer


  def get(self, request,device_auth,format=None):
    if auth_required(device_auth) == True:
      lyrics_albums = LyricsAlbum.objects.all()
      if not lyrics_albums:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      lyrics_albums_serializer = LyricsAlbumSerializer(lyrics_albums, many=True,context={'device_key': device_auth}
).data
      return Response(lyrics_albums_serializer, status=status.HTTP_200_OK)
    else:
      return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)

class SongsView(APIView):
  parser_classes = (parsers.MultiPartParser, parsers.FormParser,) 
  serializer_class = SongsSerializer

  def get(self,request,album_id,device_auth,format=None):
    if auth_required(device_auth) == True:
      album = Albums.objects.get(id=album_id)
      songs = Songs.objects.filter(album=album)
      if not songs:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      songs_serializer = SongsSerializer(songs, many=True,context={'device_key': device_auth}
).data
      return Response(songs_serializer, status=status.HTTP_200_OK)
    else:
      return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)



class SongLyricsView(APIView):
  parser_classes = (parsers.MultiPartParser, parsers.FormParser,) 
  serializer_class = SongsLyricsSerializer

  def get(self,request,album_id,device_auth,format=None):
    if auth_required(device_auth) == True:
      album = LyricsAlbum.objects.get(id=album_id)
      song_lyrics = SongLyrics.objects.filter(album=album)
      if not song_lyrics:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      songs_lyrics_serializer = SongsLyricsSerializer(song_lyrics, many=True,context={'device_key': device_auth}
).data
      return Response(songs_lyrics_serializer, status=status.HTTP_200_OK)
    else:
      return Response({"ERROR":"Access Denied"}, status=status.HTTP_404_NOT_FOUND)


class TriggerYoutubeCrawlerJobView(APIView):

  def crawl_youtube(msg):
    os.system("python manage.py youtube_song_crawl")
  
  def get(self,request,format=None):
    Thread(target=self.crawl_youtube, args=("")).start()
    return Response({"Message": "O.K."}, status=status.HTTP_200_OK)