# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0026_auto_20181025_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passenger',
            field=models.CharField(default='user', max_length=255),
            preserve_default=False,
        ),
    ]
