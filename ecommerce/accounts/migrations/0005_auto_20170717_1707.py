# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-17 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170717_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
