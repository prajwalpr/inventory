# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 09:25
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190109_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=30, validators=[blog.validators.PhoneValidators()]),
        ),
    ]
