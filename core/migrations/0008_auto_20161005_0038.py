# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 00:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161005_0032'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('year',)]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollmentmodel',
            unique_together=set([('brand', 'model')]),
        ),
        migrations.AlterUniqueTogether(
            name='model',
            unique_together=set([('brand', 'name')]),
        ),
    ]
