from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.utils.timezone import utc
import datetime

# Create your models here.
class Story(models.Model):
    content = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def get_time_diff(self):
        if self.time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.time
            seconds = timediff.total_seconds()
            minutes = int(seconds/60)
            hours = int(minutes/60)
            days = int(hours/60)
            if seconds < 60:
                return "Less than a minute ago"
            elif seconds < 120:
                return "1 minute ago"
            elif seconds < 3600:
                return str(minutes)+ " minutes ago"
            elif seconds < 7200:
                return "1 hour ago"
            elif seconds < 86400:
                return str(hours) + " hours ago"
            elif days < 2:
                return "1 day ago"
            else:
                return str(days) + " days ago"
