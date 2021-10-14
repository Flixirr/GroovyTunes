from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.userName

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating_sum = models.IntegerField()
    rating_number = models.IntegerField()
    # extra elements needed in Playlist
    # spotify_id = models.CharField(max_length=100)
    # description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    voting = models.IntegerField()

class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    rating = models.IntegerField()