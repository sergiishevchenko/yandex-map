import requests
import uuid

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, ImagePlace


class Command(BaseCommand):
    help = 'Upload new places from json files'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='New place link')

    def handle(self, *args, **kwargs):
        response = requests.get(kwargs['link'])
        try:
            response.raise_for_status()
        except Exception as e:
            return 'Ошибка при загрузке новой локации: {}'.format(e)

        raw_place = response.json()
        place, created = Place.objects.get_or_create(
            title=raw_place['title'],
            lng=raw_place['coordinates']['lng'],
            lat=raw_place['coordinates']['lat'],
            defaults={
                'description_short': raw_place.get('description_short', ''),
                'description_long': raw_place.get('description_long', '')
            },
        )
        if created:
            for img in raw_place.get('imgs', []):
                image_response = requests.get(img)
                try:
                    image_response.raise_for_status()
                except Exception as e:
                    return 'Ошибка при загрузке новой фотографии: {}'.format(e)
                content_file = ContentFile(image_response.content, '{}'.format(uuid.uuid4()))
                ImagePlace.objects.create(place=place, image=content_file)
