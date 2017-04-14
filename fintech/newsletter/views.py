from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from django.contrib.auth.models import Group, Permission
from newsletter.forms import ReportForm, GroupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from newsletter.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError

#------------------Home------View-----------------------------------
@login_required
def homeView(request):
    user = request.user
    return render(request, 'home.html', {'user': user})
 #   if request.method == 'POST':
  #      form = 

#=---------------Login--------View---------------------------------
def invalid(request):
    return render(request, 'invalid.html')
        

  
#------------------SignUp---View------------------------------------

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            usertype = request.POST.get('usertype')
            try:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                site_user = SiteUser.objects.create(user=new_user,usertype=usertype)
                setattr(site_user, 'password', password)
            except IntegrityError:
                return HttpResponseRedirect('/invalid/')
            
            #login(request, new_user)
            #return render(request, 'results.html', {'username': form.cleaned_data['username'],
            #'email': form.cleaned_data['email']
            #                                       })

            return HttpResponseRedirect('/login/')

    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

#-------------------ViewReports----view------------------------------
@login_required
def viewReports (request):
    view = Report.objects.all()
    return render(request, 'viewReport.html', {'reports': view})
        

#-----------------newReport---view-------------------------------
@login_required
def newReport (request):
    #Report.objects.get(pk=id)
    #Report.object.all()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            """
            company = request.POST.get('companyname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            usertype = request.POST.get('usertype')
            for file in request.POST.get('files'):

            report_owner=request.user


            report =Report.

            grouplist = request.user.groups.all
            """
            form.save()
            return HttpResponseRedirect('view_report') #make this '/newsletter/reports/' if you want to redirect create report to view reports
        else:
            print(form.errors)
    else:
       form = ReportForm()
    return render(request, 'newReport.html', {'form': form})

          
# ---------------------------------------------------------------------------
#----------------------Create--Group----View--------------------------------- 
@login_required
def makeGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                groupname = request.POST.get('name')
                group = Group.objects.create(name=groupname)
                User.objects.get(username=request.user).groups.add(group)
            except IntegrityError:
                return HttpResponseRedirect('/invalidGroup/')

            #group.user_set.remove(request.user) 
            # #User.objects.get(username=request.user2add).groups.remove(group)  

            return HttpResponseRedirect('../groups/')

    else:
        form = GroupForm()

    return render(request, 'group.html', {'form': form})

@login_required
def invalidGroup(request):
    return render(request, 'invalidGroup.html')
#--------------Add-----Member----View------------------- 
@login_required
def addMember(request):
    userlist = User.objects.all()
    namelist = []
    for x in userlist:
        namelist.append(x.username)
    if request.method == 'POST':
        user_to_add = request.POST.get('submit')
        print(user_to_add)

    return render(request, 'addmembers.html',{'namelist':namelist})


#---------------Group-----Main------Page-----------------
@login_required
def viewGroups (request):
    all_groups = Group.objects.all()
    groups = []

    for x in all_groups:
        if request.user in x.user_set.all():
            groups.append(x)

    return render(request, 'groups.html', {'groups': groups})

#---------------SITE MANAGER CONTROL PANEL-----------------
@user_passes_test(lambda u: u.is_superuser)
def viewSiteManager(request):
    userlist = User.objects.all()
    namelist = []
    for x in userlist:
        if x.username != request.user.username and not x.is_superuser:
            namelist.append(x.username)
    if request.method == 'POST':
        user_to_promote = request.POST.get('submit')
        print(user_to_promote)
        user = User.objects.get(username=user_to_promote)
        user.is_superuser = True
        user.save()
        return HttpResponseRedirect('/home/')
    return render(request, 'sitemanager.html', {'namelist': namelist})