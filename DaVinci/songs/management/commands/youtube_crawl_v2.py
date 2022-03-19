import youtube_dl
import pyrebase
import os
from django.core.files import File

from django.core.files.storage import default_storage
from django.core.files import File
from django.core.management.base import BaseCommand

from DaVinci.settings import *
from songs.models import *
from authentication.models import AppParameters

config = {
  "apiKey": "AIzaSyBdRvNasADoiVlswGJWZOVlPH443Hs1yz4",
  "authDomain": "davinci-31e44.firebaseapp.com",
  "projectId": "davinci-31e44",
  "storageBucket": "davinci-31e44.appspot.com",
  "messagingSenderId": "746539869114",
  "appId": "1:746539869114:web:43b0077bb0a3e9211e3383",
  "measurementId": "G-HSZTPXFR0D",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

class Command(BaseCommand):
    help = 'Reads data from csv.'

    def download_youtube_to_mp3(self, youtube_url):
      try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = youtube_url,download=False
        )
        filename = f"media/{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        return filename
      except Exception as exp:
        print("Opps something went wrong!!!")
        print(exp)
        return False

    def save_song_to_django_model(self, song_id, filename):
        # print(filename)
        # fileMasterInstance = Songs.objects.filter(id=song_id).first()
        # openedFileinReadMode = open(filename, 'r', encoding='ISO-8859-1')
        # songFile = File(openedFileinReadMode)
        # fileMasterInstance.media_file.save(filename[6:], songFile)
        # Songs.objects.filter(id = song_id).update(crawl_required=False)
        # openedFileinReadMode.close()
        # print("Update Done now proceeding to delete the local file")
        # os.remove(str(BASE_DIR)+"/"+filename)
        path = Path(filename)
        song = Songs.objects.get(id=song_id)
        with path.open(mode='rb') as f:
            song.media_file = File(f, name=path.name)
            song.save()
        os.remove(str(BASE_DIR)+"/"+filename)


    def handle(self, *args, **options):
      if AppParameters.objects.get(parameter_name="CRAWLER_INSTANCES_COUNT").parameter_value == '0':
        AppParameters.objects.filter(parameter_name="CRAWLER_INSTANCES_COUNT").update(parameter_value='1')
        print("Running youtube crawler for Songs App!!!!")
        songs_which_need_to_be_crwaled = Songs.objects.filter(crawl_required=True)
        if len(songs_which_need_to_be_crwaled) == 0:
          print("No eligible songs to crawl !!!!!")
        else:
          print("Songs Found!!!!")
          for songs in songs_which_need_to_be_crwaled:
            filename = self.download_youtube_to_mp3(songs.song_url)
            if filename != False:
              print(filename)
              self.save_song_to_django_model(songs.id, filename)
            else:
              print("Will try for other song!!!!")
        AppParameters.objects.filter(parameter_name="CRAWLER_INSTANCES_COUNT").update(parameter_value='0')
      else:
        print("Already other instance running!, Aborting..........")
