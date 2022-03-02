import youtube_dl
import pyrebase
import os

from django.core.files.storage import default_storage
from django.core.files import File
from django.core.management.base import BaseCommand

from DaVinci.settings import *
from mantras.models import *

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

    def push_mantra_to_firebase(self, filename):
      try:
        storage.child("multimedia_files/mantras/" + filename).put(str(BASE_DIR)+"/media/"+filename)
        url = storage.child("multimedia_files/mantras/"+ filename).get_url(None)
        print("File upload in Firebase Storage successful url: {}".format(url))
        return url
      except Exception as exp:
        print(exp)
        return False

    def update_url(self, mantra_id, url, filename):
      try:
        Mantra.objects.filter(id = mantra_id).update(crawl_required=False, firebase_url = url)
        print("Update Done now proceeding to delete the local file")
        os.remove(str(BASE_DIR)+"/"+filename)
      except Exception as e:
        print("Exception at update url")
        print(e)
  
    def handle(self, *args, **options):
      print("Running youtube crawler for Mantras App!!!!")
      mantras_which_need_to_be_crwaled = Mantra.objects.filter(crawl_required=True)
      if len(mantras_which_need_to_be_crwaled) == 0:
        print("No eligible mantras to crawl !!!!!")
      else:
        print("mantras Found!!!!")
        for mantras in mantras_which_need_to_be_crwaled:
          filename = self.download_youtube_to_mp3(mantras.mantra_url)
          if filename != False:
            print(filename)
            url = self.push_mantra_to_firebase(filename[6:])
            if url != False:
              self.update_url(mantras.id, url, filename)
          else:
            print("Will try for other mantras!!!!")