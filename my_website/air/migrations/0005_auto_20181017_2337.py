# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0004_auto_20181017_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='dst',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='DST start/end'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='offset',
            field=models.FloatField(blank=True, null=True, verbose_name='Time Zone'),
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together=set([('airline', 'origin', 'destination')]),
        ),
    ]
