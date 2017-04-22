from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from .models import *
from newsletter.models import Report
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
            if s.search in v.company_name:
                super_view.append(v)
    elif s.search_type == "Lo":
        for v in view:
            if s.search in v.company_location:
                super_view.append(v)
    elif s.search_type == "Co":
        for v in view:
            if (s.search in "United States") and v.company_country == "US":
                super_view.append(v)
            elif (s.search in "Canada") and v.company_country == "CA":
                super_view.append(v)
            elif (s.search in "Great Britain") and v.company_country == "GB":
                super_view.append(v)
            elif (s.search in "Mexico") and v.company_country == "MX":
                super_view.append(v)
    elif s.search_type == "Se":
        for v in view:
            if s.search in v.sector:
                super_view.append(v)
    elif s.search_type == "Pr":
        for v in view:
            if s.search in v.projects:
                super_view.append(v)

    if request.user.is_superuser:
        return render(request, 'viewSearch.html', {'reports': super_view})
    else:
        for vi in super_view:
            if vi.is_private == 'N':
                public_view.append(vi)
    return render(request, 'viewSearch.html', {'reports': public_view})

@login_required
def viewSearch (request):
    s = Search.objects.first()
    view = Report.objects.all()
    super_view = []
    public_view = []
    for v in view:
        if (s.company_name in v.company_name or s.company_name == "") and (s.company_location in v.company_location or
           s.company_location == "") and (s.company_country == v.company_country or s.company_country == "AN") and \
           (s.sector in v.sector or s.sector == "") and (s.projects in v.projects or s.projects == "") and \
           (v not in super_view):
            super_view.append(v)

    if request.user.is_superuser:
        return render(request, 'viewSearch.html', {'reports': super_view})
    else:
        for vi in super_view:
            if vi.is_private == 'N':
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

            s.save()
            return HttpResponseRedirect('/search/view_search/')
        else:
            print(form.errors)
    else:
        form = SearchForm()
        return render(request, 'newSearch.html', {'form': form})
