from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

# Create your models here.
class Story(models.Model):
    content = models.CharField(max_length=100)