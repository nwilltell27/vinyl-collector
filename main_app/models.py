from django.db import models

# Create your models here.
class Vinyl(models.Model):
    artist = models.CharField(max_length=100)
    album_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.artist