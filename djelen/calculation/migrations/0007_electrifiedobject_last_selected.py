# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0006_auto_20161122_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrifiedobject',
            name='last_selected',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
