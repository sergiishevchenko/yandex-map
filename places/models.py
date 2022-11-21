from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=256)
    description_short = models.TextField(blank=True, null=True)
    description_long = models.TextField(blank=True, null=True)
    coordinate_lng = models.FloatField(blank=True, null=True)
    coordinate_lat = models.FloatField(blank=True, null=True)