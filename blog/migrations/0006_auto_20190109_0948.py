# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 09:48
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190109_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(validators=[blog.validators.TextValidators()]),
        ),
    ]