from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=256)
    description_short = models.TextField(blank=True, null=True)
    description_long = models.TextField(blank=True, null=True)
    coordinate_lng = models.FloatField(blank=True, null=True)
    coordinate_lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Локации"


class ImagePlace(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    place = models.ForeignKey(Place, related_name='imgs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Картинки"