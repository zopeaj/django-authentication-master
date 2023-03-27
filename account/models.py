from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
# Create your models here.

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.OneToManyField(Movie, on_delete=models.CASCADE)
    age = models.IntegerField(defaults=0)
    bio = models.TextField(default='no bio..')
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')

    def __str__(self):
        return f"{self.user.username}"

