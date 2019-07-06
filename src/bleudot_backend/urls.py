"""bleudot_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.models import User, Organization
from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
from rest_framework import viewsets, routers
from rest_framework.response import Response
from .serializers import UserViewSet, OrganizationViewSet
from django.conf.urls import url, include
from django.urls import path




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organizations', OrganizationViewSet)



urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
]
