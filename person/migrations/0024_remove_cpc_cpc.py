# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-11 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0023_auto_20180611_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpc',
            name='cpc',
        ),
    ]
