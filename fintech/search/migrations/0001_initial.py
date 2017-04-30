# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-30 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=45)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico'), ('AN', 'Any')], max_length=2)),
                ('sector', models.CharField(max_length=45)),
                ('projects', models.CharField(max_length=30)),
                ('ceo_name', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SearchBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=200)),
                ('search_type', models.CharField(choices=[('Na', 'Company Name'), ('Lo', 'Company Location'), ('Co', 'Company Country'), ('Se', 'Company Sector'), ('Pr', 'Current Project(s)'), ('Cn', 'CEO Name'), ('In', 'Industry')], max_length=3)),
            ],
        ),
    ]
