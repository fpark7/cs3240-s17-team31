# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('file', models.FileField(upload_to='reports/')),
                ('encrypted', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('owner', models.CharField(max_length=50)),
                ('ceo_name', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('company_name', models.CharField(max_length=45)),
                ('company_Phone', models.CharField(max_length=11)),
                ('company_location', models.CharField(max_length=45)),
                ('company_country', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'Great Britain'), ('MX', 'Mexico')], max_length=2)),
                ('sector', models.CharField(max_length=45)),
                ('company_email', models.EmailField(max_length=45)),
                ('industry', models.CharField(max_length=45)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('projects', models.TextField(default='project', max_length=300)),
                ('content', models.ManyToManyField(to='newsletter.File', default='none')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('usertype', models.CharField(choices=[('c', 'Company User'), ('i', 'Investor User')], max_length=1)),
                ('groups', models.ManyToManyField(to='auth.Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
