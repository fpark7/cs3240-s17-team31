import os
from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.db import models
from fintech import settings
from messenger.forms import MessageForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
from messenger.models import Message
from django.http import HttpResponseRedirect
from django.utils import encoding
from Crypto.PublicKey import RSA


# Create your views here.

@login_required
def delete (request, message_id):
    i_d = int(message_id)
    if request.user.get_username() != Message.objects.get(pk=i_d).message_to:
        return HttpResponseRedirect('/inbox/')

    Message.objects.get(pk=i_d).delete()
    return HttpResponseRedirect('/inbox/')

@login_required
def unencrypt (request, message_id):
    i_d = int(message_id)
    message = Message.objects.get(pk=i_d)
    if request.user.get_username() != Message.objects.get(pk=i_d).message_to:
        return HttpResponseRedirect('/inbox/')
    if message.is_encrypted == 'Y':
        print("HOORAY")
        PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
        file_path = os.path.join(PROJECT_PATH, 'key')
        f = open(file_path, 'rb')
        bin_key = f.read()
        obj_key = RSA.importKey(bin_key, passphrase=None)
        message.message_content = obj_key.decrypt(bytes(message.message_enc_content)).decode()
        message.is_encrypted = 'N'
        message.save()
    return HttpResponseRedirect('/inbox/')

@login_required
def viewMessages (request):
    view = Message.objects.filter(message_to=""+request.user.get_username())
    for x in view:
        print(x)
        print(x.isNew)
        if x.isNew == 'I':
            x.isNew = 'U'
        else:
            x.isNew = 'R'
        x.save()

    return render(request, 'viewMessages.html', {'messages': view})

@login_required
def newMessage (request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create()
            message.is_encrypted = request.POST.get('is_encrypted')
            message.message_to = request.POST.get('message_to')
            message.message_from = request.user.get_username()
            message.message_title = request.POST.get('message_title')
            message.message_content = request.POST.get('message_content')
            message.isNew = 'I'
            if message.is_encrypted == 'Y':
                #file_path = os.path.join(settings.STATIC_ROOT, 'data/key')
                PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
                file_path = os.path.join(PROJECT_PATH, 'key')
                f = open(file_path, 'rb')
                bin_key = f.read()
                obj_key = RSA.importKey(bin_key, passphrase=None)
                message.message_enc_content = obj_key.encrypt(str.encode(message.message_content), 0)[0]
                message.message_content = '[encrypted]'
            message.save()
            return HttpResponseRedirect('/inbox/')
        else:
            print(form.errors)
    else:
        form = MessageForm()
    return render(request, 'newMessage.html', {'form': form})

@login_required
def groupEmail(request):
    pass
