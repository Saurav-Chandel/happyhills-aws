# Generated by Django 4.0.1 on 2022-01-17 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming_treks', '0002_rename_upcomig_treks_upcoming_treks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upcoming_Road_Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='road_trip/')),
                ('trip_name', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_type', models.CharField(blank=True, max_length=100, null=True)),
                ('activities', models.CharField(blank=True, max_length=300, null=True)),
                ('group_size', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.PositiveBigIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999)])),
                ('route', models.CharField(blank=True, max_length=300, null=True)),
                ('altitude', models.CharField(blank=True, max_length=200, null=True)),
                ('total_distance_covered', models.CharField(blank=True, max_length=200, null=True)),
                ('fixed_departure', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
