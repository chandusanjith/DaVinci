from django.urls import path, include

from .views import *

urlpatterns = [
    path('MantrasAlbums/<device_auth>/', MantraAlbumView.as_view(), name='get_mantras_albums'),
    path('Mantras/<album_id>/<device_auth>/', MantraView.as_view(), name='get_mantras'),
    path('MantraLyrics/<album_id>/<device_auth>/', MantraLyricsView.as_view(), name='get_mantra_lyrics'),
]