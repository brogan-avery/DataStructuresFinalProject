from django.db import models

# aka nodes
class Location(models.Model): # locations act as nodes with the auto gen PK as an ID integer
    location = models.CharField(max_length=400)
    lat = models.DecimalField(max_digits=8, decimal_places=4)
    lon = models.DecimalField(max_digits=8, decimal_places=4)
    state = models.CharField(max_length=400)
    # distancesToOtherLocations = models.JSONField() # EX for loc 1: { distance to loc 1 : 0 miles, distance to loc 2: 50 miles}

