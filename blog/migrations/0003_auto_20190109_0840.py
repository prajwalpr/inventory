# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190109_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
