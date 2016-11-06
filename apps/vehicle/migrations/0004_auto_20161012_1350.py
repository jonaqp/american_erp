# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleimage',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_vehicleimage_vehicle', to='vehicle.Vehicle'),
        ),
    ]
