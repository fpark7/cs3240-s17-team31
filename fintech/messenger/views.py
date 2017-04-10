from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.db import models
from messenger.forms import MessageForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
from messenger.models import *
from django.http import HttpResponseRedirect#, HttpResponse

# Create your views here.

@login_required
def newMessage (request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('view_message')
        else:
            print(form.errors)
    else:
       form = MessageForm()
    return render(request, 'newMessage.html', {'form': form})