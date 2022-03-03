from rest_framework import serializers

class HoroscopeSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   sign = serializers.CharField()
   day = serializers.CharField()
   timezone = serializers.CharField()