# from main_calendar.models import Organization, User, Event
# from rest_framework import serializers, viewsets

# """
# Serializers allow us to define the shape and data types to be returned
# in the api response. https://www.django-rest-framework.org/api-guide/serializers/
# """
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile_pic_url')

# class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Organization
#         fields = ('name', 'org_type', 'mailing_address', 'created_at')

# class EventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Event
#         fields = (
#         'name',
#         'date',
#         'description',
#         'start_time',
#         'start_date',
#         'end_date',
#         'end_time',
#         'location',
#         'created_at',
#         'deleted_at',
#         'user',
#         'recurring'
#         )

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class OrganizationViewSet(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


from rest_framework import serializers

from .models import Calendar, Event

class CalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

