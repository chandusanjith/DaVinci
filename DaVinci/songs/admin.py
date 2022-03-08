from django.contrib import admin
from django.db import models

from .models import *

admin.site.register(Albums)
admin.site.register(Songs)
admin.site.register(SongLyrics)
admin.site.register(LyricsAlbum)