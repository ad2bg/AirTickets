# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0016_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='iso',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='iso3',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='nice_name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='phone_code',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
