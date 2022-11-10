from django.db import models

# Create your models here.
class profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    contact = models.CharField(max_length=10, blank=False)