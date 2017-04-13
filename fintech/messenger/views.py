from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.db import models
from messenger.forms import MessageForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
from messenger.models import Message
from django.http import HttpResponseRedirect#, HttpResponse

# Create your views here.

@login_required
def viewMessages (request):
    view = Message.objects.all()
    return render(request, 'viewMessages.html', {'Messages': view})

@login_required
def newMessage (request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create()
            message.message_from = request.user.username
            message.message_to = request.POST.get('message_to')
            message.message_title = request.POST.get('message_title')
            message.is_encrypted = request.POST.get('is_encrypted')
            message.message_content = request.POST.get('message_content')
            message.message_delete = 'N'
            message.save()
            return HttpResponseRedirect('view_message')
        else:
            print(form.errors)
    else:
        form = MessageForm()
    return render(request, 'newMessage.html', {'form': form})
