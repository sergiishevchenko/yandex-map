import requests
import uuid

from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from places.models import Place, ImagePlace

class Command(BaseCommand):
    help = 'Upload new places from json files'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='New place link')

    def handle(self, *args, **kwargs):
        response = requests.get(kwargs['link'])
        place_json = response.json()
        place, created = Place.objects.get_or_create(
            title=place_json['title'],
            description_short=place_json['description_short'],
            description_long=place_json['description_long'],
            coordinate_lng=place_json['coordinates']['lng'],
            coordinate_lat=place_json['coordinates']['lat'],
        )
        for img in place_json['imgs']:
            r = requests.get(img)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(r.content)
            img_temp.flush()

            image_place = ImagePlace.objects.create(place=place)

            image_place.image.save("{}".format(uuid.uuid4()), File(img_temp), save=True)
