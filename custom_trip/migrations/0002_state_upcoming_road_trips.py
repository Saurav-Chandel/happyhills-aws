# Generated by Django 4.0.1 on 2022-01-21 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming_treks', '0003_upcoming_road_trips'),
        ('custom_trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='upcoming_road_trips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Upcoming_Road_Trips', to='upcoming_treks.upcoming_road_trips'),
        ),
    ]
