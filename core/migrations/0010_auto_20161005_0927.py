# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161005_0849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='type_transport',
            new_name='unit_transport',
        ),
    ]
