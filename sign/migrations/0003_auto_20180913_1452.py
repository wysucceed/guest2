# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-13 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20180913_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
