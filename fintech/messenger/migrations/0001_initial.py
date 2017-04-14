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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_encrypted', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('message_title', models.CharField(max_length=45)),
                ('message_content', models.CharField(max_length=300)),
                ('message_from', models.CharField(max_length=100)),
                ('message_to', models.CharField(max_length=100)),
                ('message_delete', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
