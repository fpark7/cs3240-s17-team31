# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('match', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('is_private', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('company_name', models.CharField(max_length=45)),
                ('company_Phone', models.CharField(max_length=11)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(max_length=2, choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico')])),
                ('sector', models.CharField(max_length=45)),
                ('projects', models.CharField(max_length=30)),
            ],
        ),
    ]
