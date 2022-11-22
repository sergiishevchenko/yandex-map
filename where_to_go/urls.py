from django.contrib import admin
from django.urls import path
from cards.views import show_card

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_card),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
