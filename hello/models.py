from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=1000)
    availability = models.BooleanField() 
    category = models.CharField(max_length=1000)
    day = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()

# class Timmings(models.Model):
#     name = models.CharField(max_length=1000)
#     availability = models.BooleanField() 
#record = Item(name="jimmy")
#record.save()
