# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20161005_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel',
            name='unit_transport',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='core_fuel_type_transport', to='core.UnitMeasurement'),
            preserve_default=False,
        ),
    ]
