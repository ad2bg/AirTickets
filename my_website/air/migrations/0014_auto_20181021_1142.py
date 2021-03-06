# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0013_auto_20181021_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routes', to='air.Airline'),
        ),
        migrations.AlterField(
            model_name='route',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routes_arriving', to='air.Airport'),
        ),
        migrations.AlterField(
            model_name='route',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routes_departing', to='air.Airport'),
        ),
    ]
