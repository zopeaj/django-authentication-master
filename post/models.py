from django.db import models
from account.models import Account

# Create your models here.
class Post(models.Model):
    id = models.PrimaryKeyField(nullable=False)
    message = models.CharField(default='', nullable=False)
    datetime = models.DateTimeField(auto_add_now=True, nullable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
