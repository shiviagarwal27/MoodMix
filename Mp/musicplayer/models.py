from django.db import models


# Create your models here.

class MusicDB(models.Model):
    song_id = models.BigAutoField(primary_key=True)
    song_name = models.CharField(max_length=500)
    song_artist = models.CharField(max_length=500)
    movie_name = models.CharField(max_length=500)
    song_category = models.CharField(max_length=500,default="General")
    emotions = models.CharField(max_length=50000,default="General")
    emojies = models.CharField(max_length=500,default="General")
    song = models.FileField(upload_to="songs", default="songs")
    image = models.ImageField(upload_to="image", default="image")

    def __str__(self):
        return self.song_name


class Contact(models.Model):
    msg_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.email
