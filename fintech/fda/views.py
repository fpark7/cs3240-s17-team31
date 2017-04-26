from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db import IntegrityError
from newsletter.models import *
import os
import json

@csrf_exempt
def fdaLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request, user) # actually does nothing
        return JsonResponse({'verification': True})
    else:
        return JsonResponse({'verification': False})

@csrf_exempt
def getReportsList(request):
    username = request.POST.get('username')
    user = User.objects.get(username=username)
    reports = Report.objects.all()
    viewable_reports = []
    if user.is_superuser:
        for report in reports:
            viewable_reports.append(report)
    else:
        for report in reports:
            if report.is_private == 'N' or report.group in user.groups.all() or report.owner == user.username:
                viewable_reports.append(report)

    data = {}
    reports_list = []
    for report in viewable_reports:
        # ADD INDUSTRY ONCE WE UPDATE THE MODEL AND FORMS
        # I am also passing report.id to be smart
        # content will be downloaded upon request in the client fda later
        content_list = []
        for file_obj in report.content.all():
            content_list.append(file_obj.file.name)
        r_dict = {'owner': report.owner, 'group': report.group, 'timestamp': report.timestamp,
                  'is_private': report.is_private, 'company_name': report.company_name, 'company_phone': report.company_Phone,
                  'company_location': report.company_location, 'company_country': report.company_country,
                  'sector': report.sector, 'projects': report.projects, 'is_encrypted': report.is_encrypted,
                  'id': report.id, 'content': content_list}

        reports_list.append(r_dict)
    data['reports_list'] = reports_list

    return JsonResponse({'reports_list': reports_list})
