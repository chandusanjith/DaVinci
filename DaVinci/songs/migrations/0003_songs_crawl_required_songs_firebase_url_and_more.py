# Generated by Django 4.0.2 on 2022-03-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_albums_album_cover_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='crawl_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='songs',
            name='firebase_url',
            field=models.CharField(default=' ', max_length=2000),
        ),
        migrations.AlterField(
            model_name='songs',
            name='song_url',
            field=models.CharField(default=' ', max_length=2000),
        ),
    ]
