# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_team_module'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teammodule',
            unique_together=set([('team', 'module')]),
        ),
    ]
