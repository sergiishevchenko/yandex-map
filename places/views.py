from django.shortcuts import render
from .models import Place

def show_card(request):
    moscow_legends = Place.objects.get(id=1)
    roof24 = Place.objects.get(id=2)
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [ moscow_legends.coordinate_lng, moscow_legends.coordinate_lat]
                },
                "properties": {
                    "title": moscow_legends.title,
                    "placeId": moscow_legends.id,
                    "detailsUrl": ""
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [roof24.coordinate_lng, roof24.coordinate_lat]
                },
                "properties": {
                    "title": roof24.title,
                    "placeId": roof24.id,
                    "detailsUrl": ""
                }
            }
        ]
    }
    return render(request, 'index.html', context={"places":places})