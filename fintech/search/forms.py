from django import forms
# from django.contrib.auth.models import User
from search.models import Search

class SearchForm(forms.Form):

    COUNTRIES = (('US', 'United States'),
                 ('CA', 'Canada'),
                 ('GB', 'Great Britain'),
                 ('MX', 'Mexico'),)

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'),)

    # owner = models.CharField(required=False, label="Enter Owner")
    match = forms.ChoiceField(required=False, choices=OPTIONS, label="Match All fields?")
    is_private = forms.ChoiceField(required=False, choices=OPTIONS)
    company_name = forms.CharField(required=False, label="Enter Company Name")
    company_Phone = forms.CharField(required=False, label="Enter Company Phone")
    company_location = forms.CharField(required=False, label="Enter Company Location")
    company_country = forms.ChoiceField(required=False, choices=COUNTRIES)
    sector = forms.CharField(required=False, label="Company Sector")
    projects = forms.CharField(required=False, label="Enter Project")

    class Meta:
        model = Search
        fields = ("match", "is_private", "company_name", "company_Phone", "company_location", "company_country"
                  , "sector", "projects")
