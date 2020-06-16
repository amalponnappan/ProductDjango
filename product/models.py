from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()

