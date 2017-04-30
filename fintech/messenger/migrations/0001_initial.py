# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-30 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_encrypted', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('message_title', models.CharField(max_length=45)),
                ('message_content', models.CharField(max_length=500)),
                ('message_from', models.CharField(max_length=100)),
                ('message_to', models.CharField(max_length=100)),
                ('message_enc_content', models.BinaryField()),
                ('isNew', models.CharField(max_length=1)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
