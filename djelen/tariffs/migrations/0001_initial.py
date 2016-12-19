# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 19:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_1_limit', models.PositiveIntegerField()),
                ('tariff_2_limit', models.PositiveIntegerField()),
                ('tariff_1', models.FloatField()),
                ('tariff_2', models.FloatField()),
                ('tariff_3', models.FloatField()),
                ('date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
