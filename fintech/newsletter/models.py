from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.utils.timezone import utc
import datetime

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(choices = (('c','Company User'),('i','Investor User'),), max_length=1)

    groups = models.ManyToManyField(Group)


    def timeStamp(self):
        return self.user.date_joined
        #return self.user.date_joined

#    @receiver(post_save,sender=User)
#    def create_user(sender,instance,created,**kwargs):
#        if created:
#            SiteUser.objects.create(user=instance)
            
#    @receiver(post_save,sender=User)
#    def save_user(sender,instance,**kwargs):
#       instance.siteuser.save()


    




# -----------------------------Report Model----------------------------


class File(models.Model):
    YESNO = (('Y', 'Yes'),
             ('N', 'No'),)

    file = models.FileField(upload_to='reports/')
    encrypted = models.CharField(max_length=1, choices=YESNO)

#class Project(models.Model):
#    project_name = models.CharField(max_length=30)
#
#    def __str__(self):
#        return self.project_name

class Report(models.Model):

    COUNTRIES= (('US', 'United States'),
                ('CA', 'Canada'),
                ('GB', 'Great Britain'), ('MX', 'Mexico'),)

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'),)

    owner = models.CharField(max_length=50)
    ceo_name = models.CharField(max_length=30)
    group = models.CharField(max_length=30, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_private = models.CharField(max_length=1, choices=OPTIONS)
    company_name = models.CharField(max_length=45)
    company_Phone = models.CharField(max_length=11)
    company_location = models.CharField(max_length=45)
    company_country = models.CharField(max_length=2, choices=COUNTRIES)
    sector = models.CharField(max_length=45)
    industry = models.CharField(max_length=45)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    projects = models.TextField(max_length=300, default='project')

    content = models.ManyToManyField(File, default="none")


    def get_time_diff(self):
        if self.time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.time
            seconds = timediff.total_seconds()
            minutes = int(seconds/60)
            hours = int(minutes / 60)
            days = int(hours / 60)
            if hours < 24:
                return 1
            elif days < 7:
                return 2
            elif days < 31:
                return 3
            else:
                return 4

    
#--------------------------------Group---Model----------------------------
#class Group(models.Model):
#    name = models.CharField(max_length=40,blank=False)
    
#    members = models.ManyToManyField(SiteUser)

#-------------------------------------END----------------------------
