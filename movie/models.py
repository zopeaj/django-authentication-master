from django.db import models
from account.models import Account
from comment.models import Comment


# Create your models here.
class Movie(models.Model):
    name = models.TextField(default='')
    year = models.DateField()
    likes = models.IntegerField()
    video_thumbnail = models.FileField(upload_to='media', default=None)
    category = models.CharField(default='', max_length=50)
    comment = models.OneToManyField(Comment, on_delete=models.CASCADE)
