from django.db import models

class Albums(models.Model):
  album_name = models.CharField(max_length=200, unique=True)
  artist = models.CharField(max_length=200, unique=True)
  album_cover_image = models.FileField(upload_to='album_cover_image/', blank=True, null=True)
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)
  
  def __str__(self):
      return self.album_name


class Songs(models.Model):
  album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='Albums_songs_fk', null=True)
  song_image = models.FileField(upload_to='song_image/', blank=True, null=True)
  song_name = models.CharField(max_length=40, default=" ")
  artist = models.CharField(max_length=40, default=" ")
  media_file = models.FileField(upload_to='songs_mp3/', blank=True, null=True)
  song_url = models.CharField(max_length=200, default=" ")
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.song_name

class SongLyrics(models.Model):
  album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='Song_Lyrics_fk', null=True)
  song_lyric_image = models.FileField(upload_to='song_image/', blank=True, null=True)
  song_name = models.CharField(max_length=40, default=" ")
  artist = models.CharField(max_length=40, default=" ")
  lyrics = models.TextField()
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.song_name