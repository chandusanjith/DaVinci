from django.db import models

class DeviceAuth(models.Model):
  device_key = models.CharField(max_length=16, default=" ")
  mapped_key = models.CharField(max_length=16, default=" ")
  updated_at = models.DateField(auto_now_add=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.device_key

class AppParameters(models.Model):
  parameter_name = models.CharField(max_length=100, default=" ")
  parameter_value = models.CharField(max_length=100, default=" ")
  updated_at = models.DateField(auto_now_add=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.parameter_name
