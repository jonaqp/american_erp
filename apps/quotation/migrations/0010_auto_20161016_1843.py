# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0009_auto_20161016_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationstoredetail',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quotationstoredetail',
            name='unit',
        ),
    ]