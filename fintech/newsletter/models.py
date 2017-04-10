from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(choices = (('c','Company User'),('i','Investor User'),), max_length=1)

#    @receiver(post_save,sender=User)
#    def create_user(sender,instance,created,**kwargs):
#        if created:
#            SiteUser.objects.create(user=instance)
            
#    @receiver(post_save,sender=User)
#    def save_user(sender,instance,**kwargs):
#       instance.siteuser.save()


    




# -----------------------------Report Model----------------------------
class Report(models.Model):
    
    COUNTRIES= (('US', 'United States'),
                ('CA', 'Canada'),
                ('GB', 'Great Britain'),
                ('MX', 'Mexico'),)

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'),)

    owner = models.CharField(max_length=45)
    
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_private = models.CharField(max_length=1, choices=OPTIONS)
    company_name = models.CharField(max_length=45)
    company_Phone = models.CharField(max_length=11)
    company_location = models.CharField(max_length=45)
    company_country = models.CharField(max_length=2, choices=COUNTRIES)
    sector = models.CharField(max_length=45)

    #class Meta:
     #   order_with_respect_to = 'company_name'


class Projects(models.Model):
    project_name = models.CharField(max_length=45)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    #class Meta:
     #   order_with_respect_to = 'project_name'

    def __str__(self):
        return self.project_name
    

class Files(models.Model):

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'))
    
    file_name=models.CharField(max_length=45)
    is_encrypted=models.CharField(max_length=1, choices=OPTIONS)
    document= models.FileField(upload_to='documents/')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, blank=True)

    #class Meta:
     #   order_with_respect_to = 'file_name'
    
    def __str__(self):
        return self.file_name
    
#-------------------------------------END----------------------------
