# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0025_auto_20181024_1707'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set([('code', 'flight_class')]),
        ),
    ]