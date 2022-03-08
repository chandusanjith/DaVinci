from django.urls import path, include

from .views import *

urlpatterns = [
    path('SongAlbums/<device_auth>/', AlbumsView.as_view(), name='get_song_albums'),
    path('LyricAlbums/<device_auth>/', LyricsAlbumView.as_view(), name='get_lyrics_albums'),
    path('DevotionalSongs/<album_id>/<device_auth>/', SongsView.as_view(), name='get_songs'),
    path('SongLyrics/<album_id>/<device_auth>/', SongLyricsView.as_view(), name='get_song_lyrics'),
]