from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_places(request):
    features = []
    for place in Place.objects.all():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail_info', args=[place.id])
            }
        }
        features.append(feature)

    places = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'index.html', context={'places': places})


def place_detail_info(request, pk):
    place = get_object_or_404(Place, pk=pk)
    update_imgs = [img.image.url for img in place.imgs.all()]

    json_response = {
        'title': place.title,
        'imgs': update_imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(json_response, json_dumps_params={'indent': 4, 'ensure_ascii': False})
