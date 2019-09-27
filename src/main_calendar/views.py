# from main_calendar.models import User, Organization
# from rest_framework import viewsets
# from .serializers import UserSerializer, OrganizationSerializer

# Create your views here.

from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer
from rest_framework import generics, response
from django.views import generic
from rest_framework.response import Response

class CalendarList(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, pk, *args, **kwargs) :
        event = Event.objects.get(pk = pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)



    


