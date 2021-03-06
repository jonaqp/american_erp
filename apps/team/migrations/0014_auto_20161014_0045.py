# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_remove_team_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='current_status',
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='team',
            name='current_status',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group',
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('name',)]),
        ),
    ]
