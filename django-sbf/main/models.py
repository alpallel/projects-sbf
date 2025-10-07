from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)

    user_description = models.TextField() # OPT
    
class Items(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True)
    price = models.IntegerField()
    
    stock = models.IntegerField() # OPT
    seller = models.ForeignKey(to=User, on_delete=models.CASCADE) # OPT

class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=Items)