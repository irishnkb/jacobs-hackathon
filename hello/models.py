from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=1000)
    availability = models.BooleanField() 

class Timmings(models.Model):
    day = models.CharField(max_length=1000),
    date = models.DateField(),
    time = models.TimeField(),
#record = Item(name="jimmy")
#record.save()
