# Generated by Django 4.1.1 on 2023-03-28 08:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_category', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(default='images-2.jpg', null=True, upload_to='')),
                ('thank_you_text', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hide', models.BooleanField(default=False)),
                ('open_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 1, 0, 0), null=True)),
                ('close_date', models.DateTimeField()),
                ('category', models.ManyToManyField(blank=True, to='events.categories')),
                ('participants', models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('jason_content', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='EventPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, unique=True)),
                ('phone', models.IntegerField(blank=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('receiver', models.CharField(blank=True, max_length=50)),
                ('reference_number', models.PositiveIntegerField(blank=True, null=True)),
                ('due_to', models.DateField(blank=True, null=True)),
                ('account', models.CharField(blank=True, max_length=75, null=True)),
                ('special_price_offsets', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
                ('participants', models.ManyToManyField(blank=True, related_name='attendee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.payment'),
        ),
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.eventposter'),
        ),
    ]
