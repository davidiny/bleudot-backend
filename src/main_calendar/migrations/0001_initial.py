# Generated by Django 2.2.3 on 2019-07-17 01:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField()),
                ('recurring', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('org_type', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('profile_pic_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_calendar.User')),
                ('field', models.CharField(max_length=30)),
            ],
            bases=('main_calendar.user',),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_collaborator', models.BooleanField(default=False)),
                ('is_allowed', models.BooleanField(default=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.Calendar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.User')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('request', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.User')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_nums', models.BooleanField(default=False)),
                ('input_unit', models.BooleanField(default=False)),
                ('set_time', models.DateTimeField()),
                ('event', models.ManyToManyField(to='main_calendar.Event')),
                ('receiver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.User')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='signature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_calendar.User'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.Organization'),
        ),
        migrations.CreateModel(
            name='EventHost',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_calendar.User')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_calendar.Organization')),
            ],
            bases=('main_calendar.user',),
        ),
    ]
