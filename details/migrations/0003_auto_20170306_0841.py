# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20170303_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='maximum_book',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='minimum_book',
            field=models.IntegerField(default=0),
        ),
    ]
