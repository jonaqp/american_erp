# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 03:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_currency_exchangerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 9, 10), null=True),
        ),
    ]