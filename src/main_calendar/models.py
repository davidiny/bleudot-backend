#from datetime import date

import datetime
from django.utils import timezone
# from address.models import AddressField
from django.db import models
# from django.conf import settings
# from django import forms
from phone_field import PhoneField

"""
 some notes:
- Django automaticall append "_id" to the column name for foreign key attributes.
- I'm using a Django library called django-address for address field. Link is in
  settings.py
- in django, there's a field called DurationField. We could use this as a column
  instead of having columns for end_time and end_date.
- For time/date fields, auto_now_add=True makes it not modifiable. To make it
  modifiable, use default=timezone.now or default=date.today (refer to documentation)
- null=True/blank=True only needed when the field is optional
- in the future, for ForeignKey, "User" should be replaced with
  "settings.AUTH_USER_MODEL"
"""

class User(models.Model):
    email           = models.EmailField(max_length=100)
    password        = models.CharField(max_length=50)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone_number    = PhoneField() # settings.py for more info
    profile_pic_url = models.URLField()
    auth_code       = models.CharField(max_length=200, null=True)

class EventHost(User):
    organization    = models.ForeignKey('Organization', on_delete=models.CASCADE)

class Student(User):
    field           = models.CharField(max_length=30)

class Calendar(models.Model):
    name            = models.CharField(max_length=200)
    description     = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True) # sets the value of the field to current datetime when the object is created
    is_private      = models.BooleanField(default=False) # default as public?
    active          = models.BooleanField(default=True)
    published       = models.BooleanField(default=False)
    organization    = models.ForeignKey('Organization', on_delete=models.CASCADE)

class Event(models.Model):
    name            = models.CharField(max_length=200)
    date            = models.DateField(default=datetime.date.today)
    description     = models.TextField()
    start_date      = models.DateField(default=datetime.date.today)
    start_time      = models.TimeField(default=timezone.now)
    end_date        = models.DateField()
    end_time        = models.TimeField()
    location        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    calendar        = models.ForeignKey(Calendar, null=True, blank=True, on_delete=models.SET_NULL)
    recurring       = models.BooleanField(default=False) # we probably need more structure for recurring events
    type            = models.CharField(max_length=200, null=True)
    room            = models.CharField(max_length=200, null=True)
    signature       = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    


class Organization(models.Model):
    name            = models.CharField(max_length=200)
    org_type        = models.CharField(max_length=200)
    email           = models.EmailField(max_length=200)
<<<<<<< HEAD
=======
    org_type        = models.CharField(max_length=200)
>>>>>>> develop
    created_at      = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    created_at      = models.DateTimeField(default=timezone.now)
    is_owner        = models.BooleanField(default=False) # default as OWNER?
    is_collaborator = models.BooleanField(default=False) # default as view-only?
    is_allowed      = models.BooleanField(default=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar        = models.ForeignKey(Calendar, on_delete=models.CASCADE)

class Rsvp(models.Model):
    invitation      = models.BooleanField(default=False) # ???
    is_verified     = models.BooleanField(default=False)
    request         = models.BooleanField(default=False) # ???
    starred         = models.BooleanField(default=False)
    event           = models.ForeignKey(Event, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)

class Notification(models.Model):
    input_nums      = models.BooleanField(default=False) # ???
    input_unit      = models.BooleanField(default=False) # ???
    set_time        = models.DateTimeField()
    event           = models.ManyToManyField(Event)
    receiver_user   = models.ForeignKey(User, on_delete=models.CASCADE)
