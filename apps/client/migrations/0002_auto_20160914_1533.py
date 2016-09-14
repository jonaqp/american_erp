# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_person_module', to='core.Module'),
        ),
        migrations.AddField(
            model_name='person',
            name='subsidiary',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_person_subsidiary', to='core.Subsidiary'),
        ),
    ]