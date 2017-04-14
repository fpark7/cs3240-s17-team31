# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_encrypted', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('message_title', models.CharField(max_length=45)),
                ('message_content', models.CharField(max_length=300)),
                ('message_from', models.CharField(max_length=100)),
                ('message_to', models.CharField(max_length=100)),
                ('message_delete', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
