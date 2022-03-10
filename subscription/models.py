from django.db import models

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
