from django.contrib import admin
from .models import Place, ImagePlace


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)


@admin.register(ImagePlace)
class ImagePlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'place')
    ordering = ('-id', 'place')