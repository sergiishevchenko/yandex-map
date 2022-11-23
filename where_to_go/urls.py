from django.contrib import admin
from django.urls import path
from places.views import show_places, place_detail_info

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places', show_places),
    path('places/<id>', place_detail_info),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
