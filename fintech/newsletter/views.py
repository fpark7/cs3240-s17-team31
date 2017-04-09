from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from newsletter.forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from newsletter.models import *
from django.http import HttpResponseRedirect, HttpResponse

#------------------Home------View-----------------------------------
@login_required
def homeView(request):
    user = request.user
    return render(request, 'home.html', {'user': user})
 #   if request.method == 'POST':
  #      form = 

#=---------------Login--------View---------------------------------
#def login(request):
#    if request.method == 'POST':
        

  
#------------------SignUp---View------------------------------------

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            usertype = request.POST.get('usertype')

            new_user = User.objects.create(username=username, email=email, password=password)
            
            site_user = SiteUser.objects.create(username=new_user,usertype=usertype)
            
            #login(request, new_user)
            #return render(request, 'results.html', {'username': form.cleaned_data['username'],
            #'email': form.cleaned_data['email']
            #                                       })
            return HttpResponseRedirect('../login/')
              
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

#-------------------ViewReports----view------------------------------

def viewReports (request):
    view = Report.objects.all()
    return render(request, 'viewReport.html', {'reports': view})
        

#-----------------newReport---view-------------------------------

def newReport (request):
    #Report.objects.get(pk=id)
    #Report.object.all()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('view_report')
        else:
            print(form.errors)
    else:
       form = ReportForm()
    return render(request, 'newReport.html', {'form': form})

          
# ---------------------------------------------------------------------------

'''@user_passes_test(lambda u: u.is_superuser)
def siteManagerActions(request):
    #give others SM status
    #suspend or restore other access to other user's accounts
    if request.method=='POST':
        # request.POST.get('')
        users = User.objects.all()
        for user in users:


    return render(request, 'signupform.html')'''


