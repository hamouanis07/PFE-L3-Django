# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0012_matierre_responsable'),
    ]

    operations = [
        migrations.CreateModel(
            name='recours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semstre', models.CharField(choices=[('1', 'changement de groupe'), ('2', 'changement des notes')], max_length=1)),
                ('remarque', models.TextField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.etudiant')),
            ],
        ),
    ]