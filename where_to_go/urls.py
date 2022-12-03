from django.contrib import admin
from django.urls import path
from places.views import show_places, place_detail_info

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('admin/', admin.site.urls),
    path('places', show_places, name='places_list'),
    path('places/<pk>', place_detail_info, name='place_detail_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
