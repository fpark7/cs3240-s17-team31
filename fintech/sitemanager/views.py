from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from newsfeed.models import Story
from newsletter.models import *
from .forms import ReportForm, FileAddForm

@user_passes_test(lambda u: u.is_superuser)
def viewSiteManager(request):
    userlist = User.objects.all()
    list = []
    for x in userlist:
        if x.username != request.user.username and not x.is_superuser:
            list.append(x)
    if request.method == 'POST':
        code = request.POST.get('submit')[0]
        username = request.POST.get('submit')[1:]
        user = User.objects.get(username=username)
        if code == "S":
            user.is_superuser = True
            Story.objects.create(content= request.user.username + " promoted " + user.username +" to site manager")
        if code == "T":
            user.is_active = not user.is_active
        user.save()
        return HttpResponseRedirect('sm_confirm/')
    return render(request, 'sitemanager.html', {'list': list})

@user_passes_test(lambda u: u.is_superuser)
def smConfirm(request):
    return render(request, 'smConfirm.html')

@user_passes_test(lambda u: u.is_superuser)
def manageGroups(request):
    grouplist = Group.objects.all()
    return render(request, 'manageGroups.html', {'grouplist': grouplist, 'len' : len(grouplist)})

@user_passes_test(lambda u: u.is_superuser)
def groupSettings(request, group_id):
    group = Group.objects.get(pk=group_id)
    users = User.objects.all()
    usernamelist = []
    not_in = []
    if request.method == 'POST':
        if request.POST.get('submit') == "back":
            return HttpResponseRedirect('/sm_panel/manageGroups/')

        username = request.POST.get('submit')
        user = User.objects.get(username=username)
        if user in group.user_set.all():
            group.user_set.remove(user)
            Story.objects.create(content=request.user.username + " removed "+ user.username +" from the group " + group.name)
            if group.user_set.all().__len__() == 0:
                group.delete()
                return HttpResponseRedirect('../../')
        elif user not in group.user_set.all():
            user.groups.add(group)
            Story.objects.create(content=request.user.username + " added " + user.username + " to the group " + group.name )
        return HttpResponseRedirect('../'+group_id)
    for u in users:
        if u in group.user_set.all():
            usernamelist.append(u.username)
        else:
            not_in.append(u.username)
    return render(request, 'groupSettings.html', {'group': group, 'usernamelist': usernamelist, 'not_in': not_in})

@user_passes_test(lambda u: u.is_superuser)
def manageReports(request):
    reports = Report.objects.all()
    return render(request, 'manageReports.html', {'reports': reports})

@user_passes_test(lambda u: u.is_superuser)
def reportSettings(request, report_id):
    report = Report.objects.get(pk=report_id)

    if request.method == 'POST':
        if request.POST.get('submit') == 'del':
            Report.objects.get(pk=report_id).delete()
            return HttpResponseRedirect('../../')
        form = ReportForm(request.POST)
        if form.is_valid():
            report.company_name = request.POST.get('company_name')
            report.ceo_name = request.POST.get('ceo_name')
            report.industry = request.POST.get('industry')
            report.is_private = request.POST.get('is_private')
            report.company_Phone = request.POST.get('company_Phone')
            report.company_location = request.POST.get('company_location')
            report.company_country = request.POST.get('company_country')
            report.sector = request.POST.get('sector')
            report.projects = request.POST.get('projects')
            report.group = request.POST.get('group')

            report.save()
        return HttpResponseRedirect('../'+report_id)

    form = ReportForm(initial={'company_name':report.company_name, 'is_private': report.is_private,
                               'company_Phone':report.company_Phone, 'company_location': report.company_location,
                               'company_country': report.company_country, 'sector': report.sector,
                               'projects': report.projects, 'group': report.group,
                                'ceo_name': report.ceo_name, 'industry': report.industry})
    return render(request, 'reportSettings.html', {'report': report, 'form': form})

@user_passes_test(lambda u: u.is_superuser)
def fileSettings(request, report_id):
    report = Report.objects.get(pk=report_id)
    if request.method == 'POST':
        if "r" in request.POST.get('submit'):
            file_id = request.POST.get('submit')[1:]
            report.content.remove(File.objects.get(id=file_id))
            report.save()
            return HttpResponseRedirect('../' + report_id)
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
    return render(request, 'fileSettings.html', {'report': report, 'form': form})
