# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20161006_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_productmodel_brand', to='core.ProductBrand'),
        ),
    ]
