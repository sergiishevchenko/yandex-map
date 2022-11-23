from django.shortcuts import render
from .models import Place

def show_card(request):
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