# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20170801_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporterprofile',
            name='location',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]