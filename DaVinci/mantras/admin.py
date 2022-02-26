from django.contrib import admin
from django.db import models

from .models import *

admin.site.register(MantraAlbum)
admin.site.register(Mantra)
admin.site.register(MantraLyric)