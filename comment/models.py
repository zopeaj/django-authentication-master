from django.db import models
from account.models import Account
# Create your models here.

class Comment(models.Model):
    data = models.CharField(max_length=100, default=None)
    created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __init__(self):
        return f"Account with Comment {self.data}"
