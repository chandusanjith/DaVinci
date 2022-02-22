from django.contrib import admin
from django.db import models

from .models import *

admin.site.register(AppParameters)
admin.site.register(DeviceAuth)
# Register your models here.
