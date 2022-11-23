from django.shortcuts import render
from .models import Place
from django.http import Http404, HttpResponse


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
    try:
        obj = Place.objects.filter(id=id).first()
        print(obj)
    except Place.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    finally:
        return HttpResponse(obj.title)
