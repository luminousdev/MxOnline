# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-08 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20170308_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='visit_url',
        ),
    ]