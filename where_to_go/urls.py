from django.contrib import admin
from django.urls import path
from cards.views import show_card

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', show_card),
]
