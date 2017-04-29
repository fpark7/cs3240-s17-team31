from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

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
    file = models.FileField(upload_to='reports/')

#class Project(models.Model):
#    project_name = models.CharField(max_length=30)
#
#    def __str__(self):
#        return self.project_name

class Report(models.Model):

    COUNTRIES= (('US', 'United States'),
                ('CA', 'Canada'),
                ('GB', 'Great Britain'),                ('MX', 'Mexico'),)

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'),)

    owner = models.CharField(max_length=50)
    group = models.CharField(max_length=30, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_private = models.CharField(max_length=1, choices=OPTIONS)
    company_name = models.CharField(max_length=45)
    company_Phone = models.CharField(max_length=11)
    company_location = models.CharField(max_length=45)
    company_country = models.CharField(max_length=2, choices=COUNTRIES)
    sector = models.CharField(max_length=45)
    industry = models.CharField(max_length=45)

    projects = models.TextField(max_length=300, default='project')

    content = models.ManyToManyField(File, default="none")
    is_encrypted=models.CharField(max_length=1, choices=OPTIONS)


    #class Meta:
     #   order_with_respect_to = 'company_name'

    # def setOwner(self, name):
    #     self.owner = name

    
#--------------------------------Group---Model----------------------------
#class Group(models.Model):
#    name = models.CharField(max_length=40,blank=False)
    
#    members = models.ManyToManyField(SiteUser)

#-------------------------------------END----------------------------
