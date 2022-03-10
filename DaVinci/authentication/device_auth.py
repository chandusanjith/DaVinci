from datetime import date

from .models import *
from .views import DeviceLogin


def auth_required(auth_key):
  if len(auth_key) != 16:
    return False
  if DeviceAuth.objects.filter(device_key=auth_key).exists():
    device_instance = DeviceAuth.objects.filter(device_key=auth_key).first()
    if DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).exists():
        data = DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).first()
        DeviceLoginLog.objects.filter(device=device_instance, date=date.today()).update(logged_count=data.logged_count + 1)
    else:
        DeviceLoginLog.objects.create(device=device_instance, logged_count=1)
    return True
  else:
    return False