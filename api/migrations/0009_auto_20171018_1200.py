# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171018_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expected_cal',
            field=models.IntegerField(default=1000, help_text='Expected number of calories per day'),
        ),
    ]