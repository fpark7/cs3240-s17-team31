from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.db import models
from django.contrib.auth.models import Group, Permission
from .forms import ReportForm
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
            
            #login(request, new_user)
            #return render(request, 'results.html', {'username': form.cleaned_data['username'],
            #'email': form.cleaned_data['email']
            #                                       })
            try:
                user_exists = User.objects.get(username=request.POST['username'])
                return HttpResponse("Username already taken")
            except User.DoesNotExist:
                return HttpResponseRedirect('../login/')

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

'''@user_passes_test(lambda u: u.is_superuser)
def siteManagerActions(request):
    #give others SM status
    #suspend or restore other access to other user's accounts
    if request.method=='POST':
        # request.POST.get('')
        users = User.objects.all()
        for user in users:


    return render(request, 'signupform.html')'''


#----------------------Create--Group----View---------------------------------
def makeGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            groupname = request.POST.get('name')
        else:
            form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
            

