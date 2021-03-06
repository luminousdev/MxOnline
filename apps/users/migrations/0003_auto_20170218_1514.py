# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170218_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='\u5973', max_length=6, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u56fe\u7247'),
        ),
    ]
