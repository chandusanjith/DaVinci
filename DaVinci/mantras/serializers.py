from rest_framework import serializers

from authentication.models import DeviceAuth
from .models import *

class MantraAlbumSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = MantraAlbum
        fields = ('id','album_name','artist','album_cover_image','created_on','updated_on','auth_key')

    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key

class MantraSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Mantra
        fields = ('id','album','mantra_image','mantra_name','artist','media_file','mantra_url','mantra_url','created_on','updated_on','auth_key')

    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key


class MantraLyricsSerializer(serializers.ModelSerializer):
    auth_key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = MantraLyric
        fields = ('id','album','mantra_lyric_image','mantra_name','artist','lyrics','created_on','updated_on','auth_key')       
      
    def get_auth_key(self,request):
      device_key = self.context.get("device_key")
      mapped_key = DeviceAuth.objects.get(device_key = device_key)
      return mapped_key.mapped_key