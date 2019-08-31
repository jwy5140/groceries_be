from django.db import models

# Create your models here.

class List(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    items = models.TextField(blank=True)
