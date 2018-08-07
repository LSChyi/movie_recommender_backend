import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    email = models.EmailField(unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    training_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.id}:{self.training_id}'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return f'{self.user}:{self.movie}'
