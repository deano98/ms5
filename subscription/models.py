from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class SubType(models.Model):
    name = models.CharField(max_length=254)
    price = models.IntegerField()
    sub_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

class SubFeatures(models.Model):
    plan = models.ForeignKey(SubType, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=254)

    def __str__(self):
        return self.plan_name

class CustomUser(AbstractUser):
    customer = models.ForeignKey('djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey('djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL)
