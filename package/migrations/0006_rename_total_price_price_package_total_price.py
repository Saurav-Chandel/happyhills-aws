# Generated by Django 4.0.1 on 2022-02-05 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_package_total_price_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='total_price_price',
            new_name='total_price',
        ),
    ]
