# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='content',
        ),
        migrations.AddField(
            model_name='report',
            name='content',
            field=models.ManyToManyField(null=True, to='newsletter.File'),
        ),
    ]
