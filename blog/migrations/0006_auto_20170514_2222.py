# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='category',
        ),
    ]
