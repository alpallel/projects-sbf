from django.db import models
from django.contrib.auth.models import User
import uuid

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=20)
    user_description = models.TextField()
    user_password = models.CharField(max_length=20)
    

class Items(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    seller = models.ForeignKey(to=User, on_delete=models.CASCADE)