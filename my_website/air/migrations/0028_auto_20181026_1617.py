# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0027_ticket_passenger'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seat',
            options={'ordering': ['flight_class__flight__aircraft__name', 'flight_class__name', 'code']},
        ),
    ]