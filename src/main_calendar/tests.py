from django.test import TestCase
import datetime
from django.utils import timezone

from .models import User
from .models import Event
from .models import EventHost
from .models import Student
from .models import Subscription
from .models import Calendar
from .models import Organization
from .models import Rsvp
from .models import Notification


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            email = 'A@gmail.com',
            password = '1234',
            first_name = 'Donghun',
            last_name = 'Cho'
            )

    def test_user_test_basic(self):
        userOne = User.objects.get(email="A@gmail.com")
        self.assertEqual(userOne.email, 'A@gmail.com')
        self.assertEqual(userOne.password, '1234')
        self.assertEqual(userOne.first_name, 'Donghun')
        self.assertEqual(userOne.last_name, 'Cho')

class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            name = 'practice',
            description = 'test event',
            location = 'CMU')

    def test_event_test_basic(self):
        eventOne = Event.objects.get(name='practice')
        self.assertEqual(eventOne.name, 'practice')
        self.assertEqual(eventOne.date, datetime.date.today)
        self.assertEqual(eventOne.description, 'test event')
        self.assertEqual(eventOne.start_date, datetime.date.today)
        self.assertEqual(eventOne.start_time, timezone.now)
        self.assertEqual(eventOne.location, 'CMU')
        self.assertEqual(eventOne.recurring, False)

class OrganizationTestCase(TestCase):
    def setUp(self):
        Organization.objects.create(
            name = 'Bleudot',
            org_type = 'Project'
        )

    def test_organization_test_basic(self):
        orgOne = Organization.objects.get(name = 'Bleudot')
        self.assertEqual(orgOne.name, 'Bleudot')
        self.assertEqual(orgOne.org_type, 'Project')
        self.assertEqual(orgOne.created_at, timezone.now)

class RSVPTestCase(TestCase):
    def createUser(self):
        return User.objects.create(
            email = 'test_rsvp@gmail.com',
            password = '1234',
            first_name = 'Test_rsvp',
            last_name = 'Account'
            )

    def createEvent(self):
        return Event.objects.create(
                name = 'test_event_rsvp',
                description = 'test event',
                end_date = datetime.date.fromtimestamp(1885410404),
                end_time = datetime.time(hour=12, minute=34, second=56, microsecond=123456),
                location = 'CMU'
                )

    def createRSVP(self):
        event = self.createEvent()
        user = self.createUser()
        return Rsvp.objects.create(
            event = event,
            user = user
        )

    def test_rsvp_test_basic(self):
        rsvp = self.createRSVP()
        self.assertEqual(rsvp.invitation, False)
        self.assertEqual(rsvp.request, False)
        self.assertEqual(rsvp.starred, False)
        self.assertEqual(rsvp.user.first_name, "Test_rsvp")
        self.assertEqual(rsvp.event.name, "test_event_rsvp")

class CalendarTestCase(TestCase):
    def setUp(self):
        Calendar.objects.create(
            name = 'test',
            description = 'test'
        )

    def test_calendar_test_basic(self):
        calOne = Calendar.objects.get(name = 'test')
        self.assertEqual(calOne.name, 'test')
        self.assertEqual(calOne.description, 'test')
        self.assertEqual(calOne.is_private, False)
        self.assertEqual(calOne.active, True)
        self.assertEqual(calOne.published, False)

class SubscriptionTestCase(TestCase):

    def createOrganization(self):
        return Organization.objects.create(
                    name = 'Bleudot_SubTests',
                    org_type = 'Project_SubTests'
                )


    def createUser(self):
        return User.objects.create(
                    email = 'test@gmail.com',
                    password = '1234',
                    first_name = 'Test',
                    last_name = 'Account'
                    )

    def createCalendar(self):
        organization = self.createOrganization()
        return Calendar.objects.create(
        name = 'test_calendar',
        description = 'test_desc',
        organization = organization
        )


    def createSubscription(self):
        user = self.createUser()
        calendar = self.createCalendar()
        return Subscription.objects.create(user = user, calendar = calendar)

    def test_subscription_test_basic(self):
        testSub = self.createSubscription()
        self.assertEqual(testSub.is_owner, False)
        self.assertEqual(testSub.user.first_name, "Test")
        self.assertEqual(testSub.calendar.name, "test_calendar")
