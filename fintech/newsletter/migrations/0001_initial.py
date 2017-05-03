# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-03 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reports/')),
                ('encrypted', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('ceo_name', models.CharField(max_length=30)),
                ('group', models.CharField(blank=True, max_length=30)),
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
                ('content', models.ManyToManyField(default='none', to='newsletter.File')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('c', 'Company User'), ('i', 'Investor User')], max_length=1)),
                ('groups', models.ManyToManyField(to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
