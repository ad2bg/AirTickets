# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0011_auto_20181019_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seat',
            options={'ordering': ('flight_class__aircraft__name', 'flight_class__name', 'code')},
        ),
        migrations.AlterField(
            model_name='airline',
            name='code',
            field=models.CharField(max_length=10, unique=True, verbose_name='Airline Code'),
        ),
        migrations.AlterField(
            model_name='airline',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Airline Name'),
        ),
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
