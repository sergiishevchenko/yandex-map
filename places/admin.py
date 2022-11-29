from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Place, ImagePlace
from adminsortable2.admin import SortableAdminBase, SortableTabularInline


class ImagePlaceInline(SortableTabularInline):
    model = ImagePlace
    extra = 0
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        output = format_html('<img src="{0}" style="height: {1}px"/>', obj.image.url, 200)
        return mark_safe(output)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    inlines = (ImagePlaceInline,)
