# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 03:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20161004_1216'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together=set([('menu', 'reference')]),
        ),
    ]