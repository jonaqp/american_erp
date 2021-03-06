# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('team', '0003_auto_20161006_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('current_status', models.CharField(choices=[('', '--Choose--'), ('ENABLED', 'Enabled'), ('DISABLED', 'Disabled')], default='ENABLED', max_length=10)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_team_group', to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TeamModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Module')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='groupmodule',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='groupmodule',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmodule',
            name='module',
        ),
        migrations.DeleteModel(
            name='GroupModule',
        ),
        migrations.AddField(
            model_name='team',
            name='module',
            field=models.ManyToManyField(through='team.TeamModule', to='team.Module'),
        ),
    ]
