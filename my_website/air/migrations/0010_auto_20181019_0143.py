# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0009_auto_20181019_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
