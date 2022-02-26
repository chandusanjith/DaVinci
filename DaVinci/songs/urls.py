from django.urls import path, include

from .views import *

urlpatterns = [
    path('Albums/<device_auth>/', Albums.as_view(), name='get_albums'),
    path('Songs/<album_id>/<device_auth>/', Songs.as_view(), name='get_songs'),
    path('SongLyrics/<album_id>/<device_auth>/', SongLyrics.as_view(), name='get_song_lyrics'),
]