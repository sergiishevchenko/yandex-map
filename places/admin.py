from django.contrib import admin
from .models import Place, ImagePlace
from adminsortable2.admin import SortableAdminBase, SortableTabularInline


class ImagePlaceInline(SortableTabularInline):
    model = ImagePlace
    extra = 0
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" style="height: 200px"/>'.format(obj.image.url))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    inlines = (ImagePlaceInline,)