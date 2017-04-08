# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file_name', models.CharField(max_length=45)),
                ('is_encrypted', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('project_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('owner', models.CharField(max_length=45)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('company_name', models.CharField(max_length=45)),
                ('company_Phone', models.CharField(max_length=11)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(max_length=2, choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico')])),
                ('sector', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='report',
            field=models.ForeignKey(to='newsletter.Report'),
        ),
        migrations.AddField(
            model_name='files',
            name='report',
            field=models.ForeignKey(blank=True, to='newsletter.Report'),
        ),
    ]
