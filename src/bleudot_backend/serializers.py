from django.contrib.auth.models import User, Organization
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
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