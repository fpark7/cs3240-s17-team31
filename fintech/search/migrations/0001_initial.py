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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('company_name', models.CharField(max_length=45)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(max_length=2, choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico'), ('AN', 'Any')])),
                ('sector', models.CharField(max_length=45)),
                ('projects', models.CharField(max_length=30)),
                ('ceo_name', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=45)),
                ('time_created', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SearchBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('search', models.CharField(max_length=200)),
                ('search_type', models.CharField(max_length=3, choices=[('Na', 'Company Name'), ('Lo', 'Company Location'), ('Co', 'Company Country'), ('Se', 'Company Sector'), ('Pr', 'Current Project(s)'), ('Cn', 'CEO Name'), ('In', 'Industry'), ('Cp', 'Current Projects')])),
            ],
        ),
    ]
