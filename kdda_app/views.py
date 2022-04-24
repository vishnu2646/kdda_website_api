from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/event-list/',
        'Detail View':"/event-detail/<str:pk>/",
        "Create":"/event-create/",
        "Update":"/event-update/<str:pk>/",
        "Delete":"/event-delete/<str:pk>/",
    }
    return Response(api_urls)

@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()
    res = []
    for event in events:
        images = event.images.all()
        res_event = {"id":event.id, "name":event.name, "images":[]}
        for image in images:
            image_url = "http://localhost:8000" + image.image.url
            res_event["images"].append(image_url)
        res.append(res_event)
    return Response(res, status=200)

@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    images = event.images.all()
    res_event = {"id":event.id, "name":event.name, "images":[]}
    for image in images:
        res_event["images"].append(image.image.url)
    return Response(res_event)

@api_view(['POST'])
def eventCreate(request):
    event = Event(name = request.data["name"])
    event.save()
    for file in request.FILES.getlist('images'):
        image = Image(event=event, image=file)
        image.save()
    return HttpResponse("Event is Deleted...",status=200)

@api_view(['DELETE'])
def eventDelete(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return HttpResponse("Event is Deleted...",status=200)