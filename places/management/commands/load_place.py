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
            print('Ошибка при загрузке новой локации: ' + str(e))
        place_data = response.json()
        place, created = Place.objects.update_or_create(
            title=place_data['title'],
            description_short=place_data.get('description_short', ''),
            description_long=place_data.get('description_long', ''),
            lng=place_data['coordinates']['lng'],
            lat=place_data['coordinates']['lat'],
            defaults={'title': place_data['title'],
                      'description_short': place_data.get('description_short', ''),
                      'description_long': place_data.get('description_long', ''),
                      'lng': place_data['coordinates']['lng'],
                      'lat': place_data['coordinates']['lat']
                    },
        )
        if created:
            for img in place_data.get('imgs', []):
                image_response = requests.get(img)
                try:
                    image_response.raise_for_status()
                except Exception as e:
                    print('Ошибка при загрузке новой фотографии: ' + str(e))
                image_place = ImagePlace.objects.create(place=place)
                image_place.image.save('{}'.format(uuid.uuid4()), ContentFile(image_response.content))
