from django.db import models

class HoroscopeUsersLog(models.Model):
  device_key = models.CharField(max_length=16, default=" ")
  day = models.CharField(max_length=16, default=" ")
  sign = models.CharField(max_length=16, default=" ")
  language = models.CharField(max_length=16, default=" ")
  timezone = models.DateField(auto_now_add=True)
  out_message = models.TextField()
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)
  

  def __str__(self):
      return self.device_key