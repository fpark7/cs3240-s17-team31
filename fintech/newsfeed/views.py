from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def feed(request):
    stories = Story.objects.all()

    return render(request,'feed.html',{'stories':stories})