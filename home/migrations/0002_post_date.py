# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
