# Generated by Django 4.0.1 on 2022-06-04 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_trip', '0018_d_best_season_d_difficulty_level_d_duration_d_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='d',
            name='state',
        ),
    ]