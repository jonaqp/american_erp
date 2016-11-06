# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('core', '0014_auto_20161005_1305'),
        ('company', '0002_auto_20161005_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsidiary',
            name='store_local',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_subsidiary_store_local', to='core.Store'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='correlative',
            unique_together=set([('organization', 'subsidiary', 'type_document')]),
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together=set([('business_name', 'document_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='subsidiary',
            unique_together=set([('organization', 'store_local')]),
        ),
    ]
