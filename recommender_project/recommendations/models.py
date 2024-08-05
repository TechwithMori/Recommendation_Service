from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    preference_score = models.FloatField()


# Create your models here.
