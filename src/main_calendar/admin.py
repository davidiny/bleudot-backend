from django.contrib import admin

# Register your models here.
from .models import User
from .models import EventHost
from .models import Student
from .models import Calendar
from .models import Event
from .models import Organization
from .models import Subscription
from .models import Rsvp
from .models import Notification

admin.site.register(User)
admin.site.register(EventHost)
admin.site.register(Student)
admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(Subscription)
admin.site.register(Rsvp)
admin.site.register(Notification)
