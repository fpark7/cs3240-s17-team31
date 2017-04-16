from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from django.contrib.auth.models import Group, Permission

from .forms import ReportForm, GroupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import *
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
         

            return HttpResponseRedirect('/login/')

    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

#-------------------ViewReports----view------------------------------
@login_required
def viewReports (request):
    view = Report.objects.all()
    public_view = []
    if request.user.is_superuser:
        return render(request, 'viewReport.html', {'reports': view})
    else:
        for v in view:
            if v.is_private == 'N':
                public_view.append(v)
    return render(request, 'viewReport.html', {'reports': public_view})


#-----------------newReport---view-------------------------------
@login_required
def newReport (request):
    #Report.objects.get(pk=id)
    #Report.object.all()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():

            owner = request.user.username
            company_name = request.POST.get('company_name')
            is_private = request.POST.get('is_private')
            company_Phone = request.POST.get('company_Phone')
            company_location = request.POST.get('company_location')
            company_country = request.POST.get('company_country')
            sector = request.POST.get('sector')
            is_encrypted = request.POST.get('is_encrypted')
            projects = request.POST.get('projects')
            content = request.POST.get('content')

            report = Report.objects.create(owner=owner, company_name=company_name, is_private=is_private, company_Phone=company_Phone,
            company_location=company_location, company_country=company_country, sector=sector, is_encrypted=is_encrypted,
            projects=projects, content=content)

            for afile in request.FILES.getlist('content'):
                print("here")


            report.save()

            return HttpResponseRedirect('view_report')

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

                #addee = form.cleaned_data['addee']
                #User.objects.get(addee).groups.add(group)
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
def viewGroup (request):
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

    if request.method == 'POST':
        group_to_leave = request.POST.get('submit')
        g = Group.objects.get(name=group_to_leave)
        g.user_set.remove(request.user)
        return HttpResponseRedirect('/groups/')

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
