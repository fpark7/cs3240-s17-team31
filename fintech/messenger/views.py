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
    view = Message.objects.filter(message_to=""+request.user.get_username())
    return render(request, 'viewMessages.html', {'messages': view})

@login_required
def newMessage (request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create()
            message.message_from = request.user.get_username()
            message.message_to = request.POST.get('message_to')
            message.message_title = request.POST.get('message_title')
            message.is_encrypted = request.POST.get('is_encrypted')
            message.message_content = request.POST.get('message_content')
            message.message_delete = 'N' # what is this?
            message.save()
            return HttpResponseRedirect('/inbox/')
        else:
            print(form.errors)
    else:
        form = MessageForm()
    return render(request, 'newMessage.html', {'form': form})

@login_required
def viewDetails(request):
    pass

