from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=1000)
    availability = models.BooleanField() 
    categories = models.CharField(max_length=1000)

class Timmings(models.Model):
    day = models.CharField(max_length=1000),
    date = models.DateField(),
    time = models.CharField(max_length=1000),
#record = Item(name="jimmy")
#record.save()
