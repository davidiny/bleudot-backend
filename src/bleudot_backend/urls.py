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
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework import routers
# from .serializers import UserViewSet, OrganizationViewSet, EventViewSet
# from django.urls import path
# from Event.views import EventViewSet
from django.conf.urls import url, include
from django.contrib import admin
from main_calendar.views import CalendarList, EventList





# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'organizations', OrganizationViewSet)
# router.register(r'event', EventViewSet)



urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^calendars/$', CalendarList.as_view(), name='calendar-list'),
    url(r'^events/$', EventList.as_view(), name='event-list'),
    # path('', include(router.urls)),
    # path('admin/', admin.site.urls)
]
