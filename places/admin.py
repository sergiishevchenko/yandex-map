from django.contrib import admin
from .models import Place, ImagePlace


class ImagePlaceInline(admin.TabularInline):
    model = ImagePlace
    exclude = ()
    extra = 0
    fields = ('image', 'position',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    inlines = (ImagePlaceInline,)