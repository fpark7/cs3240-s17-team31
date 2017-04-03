from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from newsletter.forms import ReportForm


def signupform (request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = User.objects.create_user(username, email, password)
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return render(request, 'results.html', {'username': form.cleaned_data['username'],
                                                   'email': form.cleaned_data['email']
                                                   })
    else:
        form = SignupForm()

    return render(request, 'signupform.html', {'form': form})

#-----------------newReport---view-------------------------------

def newReport (request):
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            render()

        else:
            form = ReportForm()
    else:
       form = ReportForm()
    return render(request, 'newReport.html', {'form': form})
    
          
