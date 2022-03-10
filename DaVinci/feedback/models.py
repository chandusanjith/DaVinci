from django.db import models

from authentication.models import DeviceAuth

class Feedback(models.Model):
  device = models.CharField(max_length=16, default="", null=False)
  email = models.CharField(max_length=100, default=" ")
  feedback_message = models.TextField()
  mobile = models.CharField(max_length=100, default=" ")
  updated_at = models.DateField(auto_now_add=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.feedback_message