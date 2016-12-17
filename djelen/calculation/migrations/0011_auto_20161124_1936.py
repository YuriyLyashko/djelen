# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0010_auto_20161123_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricitymeter',
            name='el_object',
        ),
        migrations.RemoveField(
            model_name='electrifiedobject',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lastselected',
            name='el_mtr',
        ),
        migrations.RemoveField(
            model_name='lastselected',
            name='el_obj',
        ),
        migrations.RemoveField(
            model_name='lastselected',
            name='user',
        ),
        migrations.RemoveField(
            model_name='readings',
            name='electricity_meter',
        ),
        migrations.RemoveField(
            model_name='tariffs',
            name='user',
        ),
        migrations.DeleteModel(
            name='ElectricityMeter',
        ),
        migrations.DeleteModel(
            name='ElectrifiedObject',
        ),
        migrations.DeleteModel(
            name='LastSelected',
        ),
        migrations.DeleteModel(
            name='Readings',
        ),
        migrations.DeleteModel(
            name='Tariffs',
        ),
    ]