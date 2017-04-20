from django import forms
from .models import *

class SearchForm(forms.Form):

    COUNTRIES = (('US', 'United States'),
                 ('CA', 'Canada'),
                 ('GB', 'Great Britain'),
                 ('MX', 'Mexico'),
                 ('AN', 'Any'))

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'))

    # owner = models.CharField(required=False, label="Enter Owner")
    match = forms.ChoiceField(required=False, choices=OPTIONS, label="Match All fields?")
    # is_private = forms.ChoiceField(required=False, choices=OPTIONS, label="Is Private")
    company_name = forms.CharField(required=False, label="Enter Company Name")
    company_location = forms.CharField(required=False, label="Enter Company Location")
    company_country = forms.ChoiceField(required=False, choices=COUNTRIES, label="Company Country")
    sector = forms.CharField(required=False, label="Company Sector")
    projects = forms.CharField(required=False, label="Project Name")

    class Meta:
        model = Search
        fields = ("match", "company_name", "company_location", "company_country", "sector", "projects")

class SearchBarForm(forms.Form):

    SEARCHES = (('Na', 'Company Name'),
                ('Lo', 'Company Location'),
                ('Co', 'Company Country'),
                ('Se', 'Company Sector'),
                ('Pr', 'Current Project(s)'))
                # ('Sa', 'Search All'),)

    search = forms.CharField(required=True, label="")
    search_type = forms.ChoiceField(required=True, choices=SEARCHES)

    class Meta:
        model = SearchBar
        fields = ("search", "search_type")
