from django.db import models
from users.models import GroovyUser as User

# Create your models here.

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating_sum = models.IntegerField()
    rating_number = models.IntegerField()
    # extra elements needed in Playlist
    spotify_id = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

class Rated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    rating = models.IntegerField()
