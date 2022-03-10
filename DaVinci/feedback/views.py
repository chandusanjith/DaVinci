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



class AddFeedbackView(APIView):
    def post(self, request, format=None):
        if auth_required(request.data['device']) == True:
            serializer = FeedbackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message":"O.K."}, status=status.HTTP_200_OK)
            else:
                return Response({"ERROR": "Form is not valid :("}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"ERROR": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)

class GetFeedbackView(APIView):
  serializer_class = FeedbackSerializer

  def get(self, request, device_id, format=None):
    try:
      if device_id == "all":
        feedbacks = Feedback.objects.all()
      else:
        if auth_required(device_id) == True:
          feedbacks = Feedback.objects.filter(device=device_id)
        else:
          return Response({"ERROR": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)
      if not feedbacks:
        return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
      feedback_serializer = FeedbackSerializer(feedbacks, many=True).data
      return Response(feedback_serializer, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      return Response({
          "ERROR":"OOps!! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)