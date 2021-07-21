from django.db import models
from django.urls import reverse

# Create your models here.
class Vinyl(models.Model):
    artist = models.CharField(max_length=100)
    album_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})


# Touring Model
class Touring(models.Model):
    date = models.DateField('show date')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    artist = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f'Playing at {self.venue} in {self.city}, {self.state}, on {self.date}'