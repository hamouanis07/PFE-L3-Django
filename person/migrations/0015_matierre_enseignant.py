# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0014_auto_20180604_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='matierre',
            name='enseignant',
            field=models.ManyToManyField(related_name='prof', to='person.Adminstration'),
        ),
    ]