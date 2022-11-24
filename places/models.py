from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=256)
    description_short = models.TextField(blank=True, null=True)
    description_long = HTMLField()
    coordinate_lng = models.FloatField(blank=True, null=True)
    coordinate_lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Локации"


class ImagePlace(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(Place, related_name='imgs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Картинки"
        ordering = ['position']

    @property
    def image_preview(self):
        from django.utils.html import format_html
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" style="width: 65px;" /></a>'.format(self.image.url))