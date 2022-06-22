# Generated by Django 4.0.1 on 2022-06-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_trip', '0022_d_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a',
            name='district',
        ),
        migrations.RemoveField(
            model_name='d',
            name='state',
        ),
        migrations.AddField(
            model_name='a',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='custom_trip.state'),
            preserve_default=False,
        ),
    ]