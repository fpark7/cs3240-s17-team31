from django import forms
from django.contrib.auth.models import User
from newsletter.models import Report
from newsletter.models import SiteUser
from django.contrib.auth.models import Group, Permission

class ReportForm(forms.ModelForm):
    COUNTRIES = (('US', 'United States'),
                 ('CA', 'Canada'),
                 ('GB', 'Great Britain'),
                 ('MX', 'Mexico'),)
    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'))
    GROUPS_CHOICE = ()

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.GROUPS_CHOICE = self.GROUPS_CHOICE + (('None', 'None'),)
        for group in Group.objects.all():
            self.GROUPS_CHOICE = self.GROUPS_CHOICE + ((group.name, group.name),)
        self.fields['group'].choices = self.GROUPS_CHOICE

    company_name = forms.CharField(required=True, label="Enter Company Name")
    ceo_name = forms.CharField(required=True, label="Enter CEO Name")
    industry = forms.CharField(required=True, label="Enter Industry")
    company_Phone = forms.CharField(required=True, label="Enter Company Phone Number")
    company_location = forms.CharField(required=True, label="Enter Company Location")
    company_country = forms.ChoiceField(required=True, choices=COUNTRIES, label="Enter Company Country")
    sector = forms.CharField(required=True, label="Enter Company Sector")
    group = forms.ChoiceField(label="Which Group Should This Report Be Associated With?", required=True,
                              choices=GROUPS_CHOICE)

    is_private = forms.ChoiceField(label="Is This Private?", required=True, choices=OPTIONS)
    projects = forms.CharField(required=True, label="Enter Project Name")
    #is_encrypted = forms.ChoiceField(label="Is The File Encrypted?", required=True, choices=OPTIONS)

    class Meta:
        model = Report
        fields = ("projects", "industry", "company_name", "sector", "ceo_name", "company_Phone", "company_location",
                  "company_country", "is_private")#, "is_encrypted")

class FileAddForm(forms.Form):
    content = forms.FileField(label="Upload a file here",
                              widget=forms.FileInput(attrs={'multiple': False, 'type': 'file', 'class': 'button'}),
                              required=False)
    class Meta:
        model = Report
        fields = ("content",)