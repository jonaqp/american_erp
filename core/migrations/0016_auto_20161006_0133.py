# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20161005_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_productmodel_brand', to='core.VehicleBrand')),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='productbrand',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='productmodel',
            unique_together=set([('brand', 'name')]),
        ),
    ]