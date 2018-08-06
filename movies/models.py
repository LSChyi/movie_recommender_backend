from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    poster_partial_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class MovieTrailer(models.Model):
    youtube_id = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.name}:{self.youtube_id}'
