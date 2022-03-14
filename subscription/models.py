from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubType(models.Model):
    name = models.CharField(max_length=254)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class SubFeatures(models.Model):
    plan = models.ForeignKey(SubType, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=254)

    def __str__(self):
        return self.plan_name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    user_tdee = models.IntegerField()

    def __str__(self):
        return self.user
