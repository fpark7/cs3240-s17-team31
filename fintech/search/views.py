from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from search.forms import SearchForm
from search.models import Search
from django.http import HttpResponseRedirect
from newsletter.models import Report

# Create your views here.

@login_required
def viewSearch (request):
    sea = Search.objects.all()
    view = Report.objects.all()
    super_view = []
    public_view = []
    if sea.first().match == "Y":
        for s in sea:
            for v in view:
                if (s.company_name == v.company_name or s.company_name == "") and (s.company_Phone == v.company_Phone or
                   s.company_Phone == "") and (s.company_location == v.company_location or s.company_location == "") \
                   and s.company_country == v.company_country and (s.sector == v.sector or s.sector == "") and \
                   (s.projects == v.projects or s.projects == "") and (v not in super_view):
                    super_view.append(v)
    elif sea.first().match == "N":
        for s in sea:
            for v in view:
                if s.is_private == v.is_private and (v not in super_view):
                    super_view.append(v)
                if s.company_name == v.company_name and (v not in super_view):
                    super_view.append(v)
                if s.company_Phone == v.company_Phone and (v not in super_view):
                    super_view.append(v)
                if s.company_location == v.company_location and (v not in super_view):
                    super_view.append(v)
                if s.company_country == v.company_country and (v not in super_view):
                    super_view.append(v)
                if s.sector == v.sector and (v not in super_view):
                    super_view.append(v)
                if s.projects == v.projects and (v not in super_view):
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
        al = Search.objects.all()
        for a in al:
            a.delete()
        if form.is_valid():
            s = Search.objects.create()
            # s.owner = request.user.username
            s.match = request.POST.get('match')
            s.company_name = request.POST.get('company_name')
            s.is_private = request.POST.get('is_private')
            s.company_Phone = request.POST.get('company_Phone')
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
