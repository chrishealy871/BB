# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170417_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]