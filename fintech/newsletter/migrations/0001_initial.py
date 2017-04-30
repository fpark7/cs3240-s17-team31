# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('file', models.FileField(upload_to='reports/')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('owner', models.CharField(max_length=50)),
                ('ceo_name', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('company_name', models.CharField(max_length=45)),
                ('company_Phone', models.CharField(max_length=11)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(max_length=2, choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico')])),
                ('sector', models.CharField(max_length=45)),
                ('industry', models.CharField(max_length=45)),
                ('projects', models.TextField(default='project', max_length=300)),
                ('is_encrypted', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
                ('content', models.ManyToManyField(default='none', to='newsletter.File')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('usertype', models.CharField(max_length=1, choices=[('c', 'Company User'), ('i', 'Investor User')])),
                ('groups', models.ManyToManyField(to='auth.Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
