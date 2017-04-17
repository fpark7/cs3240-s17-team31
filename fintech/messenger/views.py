from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.db import models
from messenger.forms import MessageForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
from messenger.models import Message
from django.http import HttpResponseRedirect
from django.utils import encoding
from Crypto.Cipher import ARC4
from Crypto.PublicKey import RSA
from Crypto import Random

# Create your views here.

@login_required
def delete (request, message_id):
    i_d = int(message_id)
    Message.objects.get(pk=i_d).delete()
    return HttpResponseRedirect('/inbox/')

@login_required
def unencrypt (request, message_id):
    i_d = int(message_id)
    m = Message.objects.get(pk=i_d)
    if m.is_encrypted == 'Y':
        # a = ARC4.new('01234567')
        # m.is_encrypted = 'N'
        # fro = m.message_from
        # title = m.message_title
        # co = m.message_content
        # m.message_from = a.decrypt(fro.encode())
        # m.message_title = a.decrypt(title.encode())
        # m.message_content = a.decrypt(co.encode())
        key = m.message_key
        # if type(RSA.importKey(m.message_key).decrypt(m.message_enc_from).decode('utf-8')) is str:
        #     return HttpResponseRedirect('/newsletter/reports/')

        fro = RSA.importKey(key).decrypt(m.message_enc_from)
        title = RSA.importKey(key).decrypt(m.message_enc_title)
        co = RSA.importKey(key).decrypt(m.message_enc_content)
        m.message_from = fro
        m.message_title = title
        m.message_content = co

        # m.message_from = m.message_enc_from
        # m.message_title = m.message_enc_title
        # m.message_content = m.message_enc_content
        m.save()
    # for m in Message.objects.filter(message_to=""+request.user.get_username()):
    #     if i_d == m.id:
    #         if m.is_encrypted == 'Y':

    return HttpResponseRedirect('/inbox/')

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
            message.is_encrypted = request.POST.get('is_encrypted')
            message.message_to = request.POST.get('message_to')
            message.message_from = request.user.get_username()
            message.message_title = request.POST.get('message_title')
            message.message_content = request.POST.get('message_content')
            if message.is_encrypted == 'Y':
                fro = message.message_from.encode('utf-8')
                title = message.message_title.encode('utf-8')
                co = message.message_content.encode('utf-8')

                random_generator = Random.new().read
                message.message_key = RSA.generate(1024, random_generator).exportKey()
                publickey = RSA.importKey(message.message_key).publickey()
                message.message_enc_from = publickey.encrypt(fro, 64)
                message.message_enc_title = publickey.encrypt(title, 64)
                message.message_enc_content = publickey.encrypt(co, 64)

                message.message_from = '[encrypted]'#publickey.encrypt(fro.encode('utf-8'), 64)
                message.message_title = '[encrypted]'#publickey.encrypt(title.encode('utf-8'), 64)
                message.message_content = '[encrypted]'#publickey.encrypt(co.encode('utf-8'), 64)

                # a = ARC4.new('01234567')
                # message.message_from = encoding.smart_text(a.encrypt(fro))
                # message.message_title = encoding.smart_text(a.encrypt(title))
                # message.message_content = encoding.smart_text(a.encrypt(co))
            # if message.is_encrypted == 'Y':
            #     message.message_enc_from = request.user.get_username()
            #     message.message_enc_title = request.POST.get('message_title')
            #     message.message_enc_content = request.POST.get('message_content')
            #     message.message_from = "[encrypted]"
            #     message.message_title = "[encrypted]"
            #     message.message_content = "[encrypted]"
            # else:
            #     message.message_from = request.user.get_username()
            #     message.message_title = request.POST.get('message_title')
            #     message.message_content = request.POST.get('message_content')

            message.save()
            # if type(''.join(map(str, publickey.encrypt(co.encode('utf-8'), 64)))) is str:
            #     return HttpResponseRedirect('/newsletter/reports/')
            return HttpResponseRedirect('/inbox/')
        else:
            print(form.errors)
    else:
        form = MessageForm()
    return render(request, 'newMessage.html', {'form': form})

@login_required
def viewDetails(request):
    pass
