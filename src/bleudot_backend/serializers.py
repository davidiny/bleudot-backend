from main_calendar.models import Organization, User
from rest_framework import serializers, viewsets

"""
Serializers allow us to define the shape and data types to be returned
in the api response. https://www.django-rest-framework.org/api-guide/serializers/
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile_pic_url')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'org_type', 'mailing_address', 'created_at')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
