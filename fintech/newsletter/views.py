from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from django.contrib.auth.models import Group, Permission

from .forms import ReportForm, GroupForm, FileAddForm
from search.forms import SearchBarForm
from messenger.models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import *
from newsfeed.models import Story
from search.models import SearchBar
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError

#------------------Home------View-----------------------------------
@login_required
def homeView(request):
    user = request.user
    stories = Story.objects.all()
    list = []
    newCount = 0
    view = Message.objects.filter(message_to="" + request.user.get_username())
    for message in view:
        if message.isNew == 'I':
            newCount += 1
    if len(stories) < 10:
        return render(request, 'home.html', {'user': user, 'stories': stories, 'newCount': newCount})
    else:
        for x in range(len(stories) - 10, len(stories)):
            list.append(stories[x])

    return render(request, 'home.html', {'user': user, 'stories': list, 'newCount': newCount})
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
                if site_user.usertype == "i":
                    Story.objects.create(content=new_user.username + " registered as an investor user")
                else:
                    Story.objects.create(content=new_user.username + " registered as a company user")
            except IntegrityError:
                return HttpResponseRedirect('/invalid/')


            return HttpResponseRedirect('/login/')

    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

#-------------------ViewReports----view------------------------------
@login_required
def viewReports (request):
    all_models_dict = {
        "view": []
    }
    view = Report.objects.all()
    public_view = []
    print (User.objects.get(username=request.user).groups.all())
    if request.user.is_superuser:
        all_models_dict["view"] = view
        if request.method == 'POST':
            form = SearchBarForm(request.POST)
            if isinstance(SearchBar.objects.first(), SearchBar):
                SearchBar.objects.first().delete()
            if form.is_valid():
                s = SearchBar.objects.create()
                s.search = request.POST.get('search')
                s.search_type = request.POST.get('search_type')
                s.save()
                return HttpResponseRedirect('/search/view_search2/')
            else:
                print(form.errors)
        else:
            form = SearchBarForm()
        return render(request, 'viewReport.html', {'reports': all_models_dict, 'view': form})
    else:
        for v in view:
            print("HEASLDKAJF")
            print(v.group)
            print(User.objects.get(username=request.user.username).groups.all())
            print(v.group in User.objects.get(username=request.user.username).groups.all())
            if v.is_private == 'N' or v.owner == request.user.username:
                public_view.append(v)
            for g in User.objects.get(username=request.user).groups.all():
                if v.group == g.name and v not in public_view:
                    public_view.append(v)
        all_models_dict["view"] = public_view
        if request.method == 'POST':
            form = SearchBarForm(request.POST)
            if isinstance(SearchBar.objects.first(), SearchBar):
                SearchBar.objects.first().delete()
            if form.is_valid():
                s = SearchBar.objects.create()
                s.search = request.POST.get('search')
                s.search_type = request.POST.get('search_type')
                s.save()
                return HttpResponseRedirect('/search/view_search2/')
            else:
                print(form.errors)
        else:
            form = SearchBarForm()
    return render(request, 'viewReport.html', {'reports': all_models_dict, 'view': form})


#-----------------newReport---view-------------------------------
@login_required
@user_passes_test(lambda u: u.is_superuser or u.siteuser.usertype is not 'i')
def newReport (request):
    #Report.objects.get(pk=id)
    #Report.object.all()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():

            owner = request.user.username
            company_name = request.POST.get('company_name')


            is_private = request.POST.get('is_private')
            company_Phone = request.POST.get('company_Phone')
            company_location = request.POST.get('company_location')
            company_country = request.POST.get('company_country')
            sector = request.POST.get('sector')
            ceo_name = request.POST.get('ceo_name')
            projects = request.POST.get('projects')
            company_email = request.POST.get('company_email')

            print(projects)

            #projects = ""
            #projects += request.POST.get('project')[0] # request.POST['project'][0]
            #print(projects[0])
            group = request.POST.get('group')
            industry = request.POST.get('industry')
            print(group)

            report = Report.objects.create(owner=owner, company_name=company_name, is_private=is_private, company_Phone=company_Phone,
            company_location=company_location, company_country=company_country, sector=sector, ceo_name=ceo_name,
            projects=projects, group=group, industry=industry,company_email=company_email)

            report.save()

            out = False
            number = 0
            while not out:
                afile = request.FILES.get('content' +str(number), None)
                astatus = request.POST.get('fileStatus' + str(number))
                if afile != None:
                    fileX = File.objects.create(file=afile, encrypted=astatus)
                    fileX.save()
                    report.content.add(fileX)
                    number += 1
                else:
                    out = True



            '''for afile in request.FILES.getlist('content'):
                fileX = File.objects.create(file=afile)
                FILENAME = afile.name
                fileX.save()
                report.content.add(fileX)'''

            report.save()

            user = User.objects.get(username=request.user)
            if is_private == 'N':
                Story.objects.create(content=user.username+" created a report called "+report.projects)
            return HttpResponseRedirect('view_report')

        else:
            print(form.errors)
    else:
       form = ReportForm(user=request.user)
    return render(request, 'newReport.html', {'form': form})

          
# ---------------------------------------------------------------------------
#----------------------Create--Group----View--------------------------------- 
@login_required
def newGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                groupname = request.POST.get('name')
                group = Group.objects.create(name=groupname)
                user = User.objects.get(username=request.user)
                user.groups.add(group)
                Story.objects.create(content=user.username+" created a new group called "+groupname)

            except IntegrityError:
                return HttpResponseRedirect('/invalidGroup/')


            return HttpResponseRedirect('../groups/')

    else:
        form = GroupForm()

    return render(request, 'newgroup.html', {'form': form})

@login_required
def invalidGroup(request):
    return render(request, 'invalidGroup.html')
#--------------Add-----Member----View------------------- 
@login_required
def viewGroup (request, group_id):
    group = Group.objects.get(pk=group_id)
    name = group.name
    userlist = User.objects.all()
    addlist = []
    memberlist = group.user_set.all()

    # because the url is unique, can't really give user_test.
    if request.user not in memberlist:
        return HttpResponseRedirect('/groups/')

    for x in userlist:
        if x not in group.user_set.all(): # memberlist?
            addlist.append(x.username)

    if request.method == 'POST':
        if request.POST.get('submit') == "back":
            return HttpResponseRedirect('/groups/')
        else:
            username = request.POST.get('submit')
            user = User.objects.get(username=username)
            adder = User.objects.get(username=request.user)
            user.groups.add(group)
            Story.objects.create(content=adder.username+" added "+user.username+" to "+ name)
            return HttpResponseRedirect('../'+group_id)

    return render(request, 'group.html',{'addlist':addlist, 'memberlist':memberlist,'name':name})


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
        Story.objects.create(content=request.user.username + " left the group " + g.name)
        if g.user_set.all().__len__() == 0:
            g.delete()
        return HttpResponseRedirect('/groups/')

    return render(request, 'groups.html', {'groups': groups})

#---------------SITE MANAGER CONTROL PANEL-----------------

'''Located in sitemanager app'''

#--------------------REPORT----VIEW--------------------------
@login_required
def viewReport (request, report_id):
    report = Report.objects.get(pk=report_id)
    group_names = []
    for g in User.objects.get(username=request.user.username).groups.all():
        group_names.append(g.name)
    #security check
    if report.is_private == 'N' or report.group in group_names or report.owner == request.user.username or \
            request.user.is_superuser:
        if request.method == 'POST':
            form = FileAddForm(request.POST, request.FILES)
            if form.is_valid():
                afile = request.FILES.get('content', None)
                astatus = request.POST.get('encrypted')
                if afile != None:
                    fileX = File.objects.create(file=afile, encrypted=astatus)
                    fileX.save()
                    report.content.add(fileX)
                report.save()
            return HttpResponseRedirect('../' + report_id)
        form = FileAddForm()
        projects = report.projects
        proj_list = projects.split(",")
        return render(request, 'report.html', {'report': report, 'form': form, 'proj_list': proj_list})
    else:
        # user is trying to access report that he/she does not have rights to
        return HttpResponseRedirect('/newsletter/reports/')
