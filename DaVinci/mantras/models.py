from django.db import models

class MantraAlbum(models.Model):
  album_name = models.CharField(max_length=200, unique=True)
  artist = models.CharField(max_length=200, unique=True)
  album_cover_image = models.FileField(upload_to='mantra_album_cover_image/', blank=True, null=True)
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)
  
  def __str__(self):
      return self.album_name


class Mantra(models.Model):
  album = models.ForeignKey(MantraAlbum, on_delete=models.CASCADE, related_name='Albums_mantra_fk', null=True)
  mantra_image = models.FileField(upload_to='mantra_image/', blank=True, null=True)
  mantra_name = models.CharField(max_length=40, default=" ")
  artist = models.CharField(max_length=40, default=" ")
  media_file = models.FileField(upload_to='mantra_mp3/', blank=True, null=True)
  mantra_url = models.CharField(max_length=200, default=" ")
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.mantra_name

class MantraLyric(models.Model):
  album = models.ForeignKey(MantraAlbum, on_delete=models.CASCADE, related_name='Mantra_Lyrics_fk', null=True)
  mantra_lyric_image = models.FileField(upload_to='mantra_lyrics_image/',blank=True, null=True)
  mantra_name = models.CharField(max_length=40, default=" ")
  artist = models.CharField(max_length=40, default=" ")
  lyrics = models.TextField()
  created_on = models.DateField(auto_now_add=True)
  updated_on = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.mantra_name