# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-03 12:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20180403_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
