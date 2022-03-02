from rest_framework import serializers

from authentication.models import DeviceAuth
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Albums
        fields = ('id','album_name','artist','album_cover_image','created_on','updated_on','auth_key')

    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key

class SongsSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Songs
        fields = ('id','album','song_image','song_name','artist','media_file','song_url','firebase_url','created_on','updated_on','auth_key')

    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key


class SongsLyricsSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SongLyrics
        fields = ('id','album','song_lyric_image','song_name','artist','lyrics','created_on','updated_on','auth_key')

    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key