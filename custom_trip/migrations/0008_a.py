# Generated by Django 4.0.1 on 2022-02-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_trip', '0007_remove_destination_images_destination_package_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
