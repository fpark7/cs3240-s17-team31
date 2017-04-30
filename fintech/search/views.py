from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from .models import *
from newsletter.models import Report
from django.dispatch import receiver
from django.utils.timezone import utc
import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def viewSearchBar (request):
    s = SearchBar.objects.first()
    view = Report.objects.all()
    super_view = []
    public_view = []
    if s.search_type == "Na":
        for v in view:
            if s.search.lower() in v.company_name.lower():
                super_view.append(v)
    elif s.search_type == "Lo":
        for v in view:
            if s.search.lower() in v.company_location.lower():
                super_view.append(v)
    elif s.search_type == "Co":
        for v in view:
            if (s.search.lower() in "united states") and v.company_country == "US":
                super_view.append(v)
            elif (s.search.lower() in "canada") and v.company_country == "CA":
                super_view.append(v)
            elif (s.search.lower() in "great britain") and v.company_country == "GB":
                super_view.append(v)
            elif (s.search.lower() in "mexico") and v.company_country == "MX":
                super_view.append(v)
    elif s.search_type == "Se":
        for v in view:
            if s.search.lower() in v.sector.lower():
                super_view.append(v)
    elif s.search_type == "Pr":
        for v in view:
            if s.search.lower() in v.projects.lower():
                super_view.append(v)
    elif s.search_type == "Cn":
        for v in view:
            if s.search.lower() in v.ceo_name.lower():
                super_view.append(v)
    elif s.search_type == "In":
        for v in view:
            if s.search.lower() in v.industry.lower():
                super_view.append(v)

    if request.user.is_superuser:
        return render(request, 'viewSearch.html', {'reports': super_view})
    else:
        for vi in super_view:
            if vi.is_private == 'N' or vi.owner == request.user.username:
                public_view.append(vi)
            for g in User.objects.get(username=request.user).groups.all():
                if v.group == g.name and v not in public_view:
                    public_view.append(v)
    return render(request, 'viewSearch.html', {'reports': public_view})

@login_required
def viewSearch (request):
    s = Search.objects.first()
    view = Report.objects.all()
    super_view = []
    public_view = []
    for v in view:
        time = s.time_created.lower() == '0' or (int(s.time_created.lower()) != 4 and v.get_time_diff() < 4) or (v.get_time_diff() == 4 and int(s.time_created.lower() == 4))
        if (s.company_name.lower() in v.company_name.lower() or s.company_name == "") and (s.company_location.lower()
           in v.company_location.lower() or s.company_location == "") and (s.company_country == v.company_country or
           s.company_country == "AN") and (s.sector.lower() in v.sector.lower() or s.sector == "") and \
           (s.projects.lower() in v.projects.lower() or s.projects == "") and (s.ceo_name.lower() in v.ceo_name.lower() or s.ceo_name == "")\
            and (s.industry.lower() in v.industry.lower() or s.industry == "") and (v not in super_view) and time:
            super_view.append(v)

        # Check if Time Created Matches

    if request.user.is_superuser:
        return render(request, 'viewSearch.html', {'reports': super_view})
    else:
        for vi in super_view:
            if vi.is_private == 'N' or vi.owner == request.user.username:
                public_view.append(vi)
        for g in User.objects.get(username=request.user).groups.all():
            if vi.group == g.name and vi not in public_view:
                public_view.append(vi)
    return render(request, 'viewSearch.html', {'reports': public_view})

@login_required
def newSearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if isinstance(Search.objects.first(), Search):
            Search.objects.first().delete()
        if form.is_valid():
            s = Search.objects.create()
            # s.owner = request.user.username
            # s.match = request.POST.get('match')
            s.company_name = request.POST.get('company_name')
            # s.is_private = request.POST.get('is_private')
            s.company_location = request.POST.get('company_location')
            s.company_country = request.POST.get('company_country')
            s.sector = request.POST.get('sector')
            s.projects = request.POST.get('projects')
            s.time_created = request.POST.get('time_created')
            s.ceo_name = request.POST.get('ceo_name')
            s.industry = request.POST.get('industry')
            print(s.time_created)

            s.save()
            return HttpResponseRedirect('/search/view_search/')
        else:
            print(form.errors)
    else:
        form = SearchForm()
        return render(request, 'newSearch.html', {'form': form})
