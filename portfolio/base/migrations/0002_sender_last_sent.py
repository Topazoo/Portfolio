# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-16 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sender',
            name='last_sent',
            field=models.CharField(default=b'2018-10-16', max_length=40),
        ),
    ]