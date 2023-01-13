from django.db import models
from account.models import Account

# Create your models here.
class Address(models.Model):
    user = models.ManyToOne(Account, on_delete=models.CASCADE)
    address_book = models.CharField()
