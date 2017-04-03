# importing forms
from django import forms
from django.contrib.auth.models import User
from newsletter.models import Report

# creating our forms
class SignupForm(forms.Form): #forms.Form
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    #model = User
    username = forms.CharField(label='Enter your username', max_length=100)
    email = forms.EmailField(label='Enter your email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
            model=User
            fields=('username','email','password')


class ReportForm(forms.ModelForm):

    COUNTRIES= (('US', 'United States'),
                ('CA', 'Canada'),
                ('GB', 'Great Britain'),
                ('MX', 'Mexico'),)

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'))

    company_name = forms.CharField(required=True, help_text="Enter Company Name")
    company_Phone = forms.CharField(required=True, help_text="Enter Company Phone Number")
    company_location = forms.CharField(required=True, help_text="Enter Company location")
    company_country = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=COUNTRIES, help_text="Enter Company country")
    sector = forms.CharField(required=True, help_text="Enter Company sector")
    is_private = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS, help_text="Is this report private?")
    project = forms.CharField(required=True, help_text="Enter project name")
    
    class Meta:
        model = Report
        fields = ("sector", "company_name", "company_Phone", "company_location","company_country", "is_private", "project")
    
