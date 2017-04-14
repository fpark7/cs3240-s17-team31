from django.db import models

# Create your models here.

class Message(models.Model):

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'),)

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_encrypted = models.CharField(max_length=1, choices=OPTIONS)
    message_title = models.CharField(max_length=45)
    message_content = models.CharField(max_length=300)
    message_from = models.CharField(max_length=100)
    message_to = models.CharField(max_length=100)
    message_delete = models.CharField(max_length=1, choices=OPTIONS)

    class Meta:
        ordering = ['timestamp']
