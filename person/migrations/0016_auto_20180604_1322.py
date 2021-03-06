# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0015_matierre_enseignant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminstration',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='etudiant',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='secretaire',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='recours',
            name='accepte',
            field=models.BooleanField(default=False),
        ),
    ]
