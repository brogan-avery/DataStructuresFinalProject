from django.db import models

# class for items on list
class Item(models.Model):
    item = models.CharField(max_length=400)
    size = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    priority = models.IntegerField()

# class for the over all list
class List(models.Model):
    budget = models.IntegerField()

