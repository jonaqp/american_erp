# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20161010_1402'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='module',
        ),
    ]
