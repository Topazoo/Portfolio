# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-16 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=40)),
                ('sent_count', models.IntegerField()),
            ],
        ),
    ]
