# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-13 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
