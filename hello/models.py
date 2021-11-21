from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=1000)
    availability = models.BooleanField()
    category = models.CharField(max_length=1000, default='')

class Timing(models.Model):
    day = models.CharField(max_length=1000)
    date = models.DateField()
    opening_time = models.CharField(max_length=1000)
    closing_time = models.CharField(max_length=1000)