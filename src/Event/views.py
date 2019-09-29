# from django.contrib.auth.models import Event
# from bleudot_backend.serializers import EventSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response

# # Create your views here.
# class EventViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Event.objects.all()
#         serializer = EventSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Event.objects.all()
#         event = get_object_or_404(queryset, pk=pk)
#         serializer = EventSerializer(event)
#         return Response(serializer.data)

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
