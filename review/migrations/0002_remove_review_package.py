# Generated by Django 4.0.1 on 2022-02-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='package',
        ),
    ]