# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20180604_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='moyenne',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
