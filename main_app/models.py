from django.db import models

# Create your models here.
class Jewels(models.Model):
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=100)