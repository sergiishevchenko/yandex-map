import json

from django.shortcuts import render
from .models import Place
from django.http import HttpResponse


def show_places(request):
    features = []
    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [ place.coordinate_lng, place.coordinate_lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": ""
            }
        }
        features.append(feature)
    places = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'index.html', context={"places":places})

def place_detail_info(request, id):
    place = Place.objects.filter(id=id).first()
    update_imgs = []
    for img in list(place.imgs.all()):
        update_imgs.append(img.image.url)
    json_response = {
        "title": place.title,
        "imgs": update_imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coordinate_lat,
            "lng": place.coordinate_lng
        }
    }
    return HttpResponse(json.dumps(json_response, ensure_ascii=False, indent=4), content_type="application/json")