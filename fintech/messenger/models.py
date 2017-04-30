from django.db import models

# Create your models here.

class Message(models.Model):

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'),)

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_encrypted = models.CharField(max_length=1, choices=OPTIONS)
    message_title = models.CharField(max_length=45)
    message_content = models.CharField(max_length=500)
    message_from = models.CharField(max_length=100)
    message_to = models.CharField(max_length=100)
    message_enc_content = models.BinaryField()
    isNew = models.CharField(max_length=1)
        # I = just initialized
        # U = unread
        # R = read


    class Meta:
        ordering = ['timestamp']
