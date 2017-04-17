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
    return render(request, 'manageGroups.html', {'grouplist': grouplist})

@user_passes_test(lambda u: u.is_superuser)
def groupSettings(request, group_name):
    group = Group.objects.get(name=group_name)
    users = User.objects.all()
    usernamelist = []
    for u in users:
        if u in group.user_set.all():
            usernamelist.append(u.username)
    return render(request, 'groupSettings.html', {'usernamelist': usernamelist})


