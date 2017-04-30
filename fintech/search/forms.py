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

    TIMES = (('0', 'Any Time'),
             ('1', 'Less Than 1 Day Ago'),
             ('2', 'Less Than 1 Week Ago'),
             ('3', 'Less Than 1 Month Ago'),
             ('4', 'More Than 1 Month Ago'))

    # owner = models.CharField(required=False, label="Enter Owner")
    # match = forms.ChoiceField(required=False, choices=OPTIONS)
    # is_private = forms.ChoiceField(required=False, choices=OPTIONS, label="Is Private")
    company_name = forms.CharField(required=False, label="Enter Company Name")
    company_location = forms.CharField(required=False, label="Enter Company Location")
    company_country = forms.ChoiceField(required=False, choices=COUNTRIES, label="Company Country")
    sector = forms.CharField(required=False, label="Company Sector")
    projects = forms.CharField(required=False, label="Current Projects")
    ceo_name = forms.CharField(required=False, label="CEO Name")
    industry = forms.CharField(required=False, label="Industry")
    time_created = forms.ChoiceField(required=False, choices=TIMES, label="Time Created")

    class Meta:
        model = Search
        fields = ("company_name", "company_location", "company_country", "sector", "projects","ceo_name","industry")

class SearchBarForm(forms.Form):

    SEARCHES = (('Na', 'Company Name'),
                ('Lo', 'Company Location'),
                ('Co', 'Company Country'),
                ('Se', 'Company Sector'),
                ('Pr', 'Current Project(s)'),
                ('Cn', 'CEO Name'),
                ('In', 'Industry'),)
                # ('Sa', 'Search All'),)

    search = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Search for...'}))
    search_type = forms.ChoiceField(required=True, choices=SEARCHES, label="")

    class Meta:
        model = SearchBar
        fields = ("search", "search_type")
