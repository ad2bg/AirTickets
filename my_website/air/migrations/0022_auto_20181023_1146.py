# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0021_remove_airport_ctry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',), 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='airline',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='airlines', to='air.Country'),
        ),
    ]
