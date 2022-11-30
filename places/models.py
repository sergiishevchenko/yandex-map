from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=256)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Локации"


class ImagePlace(models.Model):
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(Place, related_name='imgs', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Картинки"
        ordering = ['position']
