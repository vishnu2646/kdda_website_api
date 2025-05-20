from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from rest_framework.decorators import api_view
from .serializers import EventSerializer
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def event_list_with_limit(request):
    events = Event.objects.all().order_by('-date')[:3]
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def event_create(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        event = serializer.save()
        return Response({
            "message": "Event created successfully.",
            "event": EventSerializer(event).data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "message": "Event creation failed.",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response({
            "message": "Event not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def event_delete(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response({
            "message": "Event deleted successfully."
        }, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response({
            "message": "Event not found."
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def send_email_api(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if not (name and message and email):
        return Response({"error": "All fields are required (name, message, email)."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        subject = f"New message from {name}"
        body = f"Sender: {name} <{email}>\n\nMessage:\n{message}"
        to_email = settings.DEFAULT_FROM_EMAIL

        email_message = EmailMessage(
            subject=subject,
            body=body,
            from_email=email,
            to=[to_email],
            cc=[email],
            reply_to=[email],
        )
        email_message.send(fail_silently=False)
        return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)