# Generated by Django 4.0.1 on 2022-06-04 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_trip', '0010_alter_district_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='district',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
