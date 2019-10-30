# from main_calendar.models import User, Organization
# from rest_framework import viewsets
# from .serializers import UserSerializer, OrganizationSerializer

# Create your views here.

from .models import (Calendar,
                     Event,
                     Organization)
from .serializers import (CalendarSerializer,
                          EventSerializer,
                          OrganizationSerializer)
from rest_framework import generics, response
from django.views import generic
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django.shortcuts import get_object_or_404

######### circular import error ###########
#from .exportEvent import main()


class CalendarList(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

class CalendarDetailView(generics.ListCreateAPIView):
    serializer_class = CalendarSerializer
    
    def get(self, request, pk, *args, **kwargs) :
        calendar = Calendar.objects.get(pk = pk)
        serializer = CalendarSerializer(calendar)
        return Response(serializer.data)

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def post(self, request, format=None):
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    
    def get(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk = pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        data = request.data.get('event')
        serializer = EventSerializer(instance=event, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            event = serializer.save()

            ########### exporting event code############
            # summary = event.name
            # views.addEvent(summary)
            ########################################

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer 
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

class OrganizationDetailView(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer

    def get(self, request, pk, *args, **kwargs):
        org = Organization.objects.get(pk = pk)
        serializer = OrganizationSerializer(org)
        return Response(serializer.data) 



    


