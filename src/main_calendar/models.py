from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

class  Calendar(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    timezone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    organization_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Organization(models.Model):
    name = models.CharField(max_length=200)
    org_type = models.CharField(max_length=200)
    mailing_address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

# This is the first model for bleudot _backend 

# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
# This is the first model for bleudot _backend 
