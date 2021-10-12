from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class GroovyUser(AbstractUser):
    def __str__(self):
        return self.email

class Playlist(models.Model):
    user = models.ForeignKey(GroovyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating_sum = models.IntegerField()
    rating_number = models.IntegerField()
    spotify_id = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(GroovyUser, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    voting = models.IntegerField()

class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
