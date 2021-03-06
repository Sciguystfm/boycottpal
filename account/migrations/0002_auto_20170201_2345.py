# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        ('boycotted', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boycottuser',
            name='boycotts',
            field=models.ManyToManyField(blank=True, to='boycotted.Boycott'),
        ),
        migrations.AddField(
            model_name='boycottuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='boycottuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
