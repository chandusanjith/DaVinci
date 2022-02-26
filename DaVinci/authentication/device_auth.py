from .models import *

def auth_required(auth_key):
  if len(auth_key) != 16:
    return False
  if DeviceAuth.objects.filter(device_key=auth_key).exists():
    return True
  else:
    return False