import requests
import uuid

from django.core.management.base import BaseCommand
from django.core.files.temp import NamedTemporaryFile
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
        place_json = response.json()
        place, created = Place.objects.update_or_create(
            title=place_json['title'],
            description_short=place_json.get('description_short', None),
            description_long=place_json.get('description_long', None),
            coordinate_lng=place_json.get('coordinates', {}).get('lng', None),
            coordinate_lat=place_json.get('coordinates', {}).get('lat', None),
        )
        for img in place_json['imgs']:
            image_request = requests.get(img)
            content_file = ContentFile(image_request.content)
            image_place = ImagePlace.objects.create(place=place)
            image_place.image.save("{}".format(uuid.uuid4()), content_file)
