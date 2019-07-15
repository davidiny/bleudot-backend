from django.contrib.auth.models import User
from main_calendar.models import Organization
from rest_framework import serializers, viewsets

"""
Serializers allow us to define the shape and data types to be returned
in the api response. https://www.django-rest-framework.org/api-guide/serializers/
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # Define the JSON fields
        fields = ('phone_num', 'address', 'last_name', 'first_name', 'role', 'active', 'password', 'email', 'linkedin', 'facebook_id', 'organization_id', 'id')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'org_type', 'mailing_address', 'created_at')


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
