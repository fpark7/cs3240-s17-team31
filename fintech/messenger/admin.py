from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_from',)
    pass
admin.site.register(Message, MessageAdmin)
