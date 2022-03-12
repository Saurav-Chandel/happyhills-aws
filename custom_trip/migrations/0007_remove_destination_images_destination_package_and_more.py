# Generated by Django 4.0.1 on 2022-02-14 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_images_package_images'),
        ('custom_trip', '0006_images_destination_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='images',
        ),
        migrations.AddField(
            model_name='destination',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_package', to='package.package'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]