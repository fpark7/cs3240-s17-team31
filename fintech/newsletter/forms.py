# importing forms
from django import forms
from django.contrib.auth.models import User
from newsletter.models import Report
from newsletter.models import SiteUser
from django.contrib.auth.models import Group, Permission



#---------------Signup-----Form-------------------------------------------
class SignupForm(forms.Form): #forms.Form
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    #model = User
    USERTYPES = (('i', 'Investor User'),
                 ('c', 'Company User'),)
    
    username = forms.CharField(label='Enter your username', max_length=100)
    email = forms.EmailField(label='Enter your email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    usertype = forms.ChoiceField(required=True, choices=USERTYPES, label="Select Your Desired User Type")
    class Meta:
            model=User
            fields=('username','email','password','usertype')


#------------------------Report--Form------------------------------------
            
class ReportForm(forms.ModelForm):

    COUNTRIES= (('US', 'United States'),
                ('CA', 'Canada'),
                ('GB', 'Great Britain'),
                ('MX', 'Mexico'),)

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'))


    company_name = forms.CharField(required=True, label="Enter Company Name")
    company_Phone = forms.CharField(required=True, label="Enter Company Phone Number")
    company_location = forms.CharField(required=True, label="Enter Company location")
    #company_country = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=COUNTRIES, help_text="Enter Company country")
    company_country = forms.ChoiceField(required=True, choices=COUNTRIES, label="Enter Company country")
    sector = forms.CharField(required=True, label="Enter Company Sector")
    is_private = forms.ChoiceField(required=True, choices=OPTIONS)
    #is_private = forms.ChoiceField(required=True, choices=OPTIONS, label="Is this report private?")
    projects = forms.CharField(required=True, label="Enter project name")
    is_encrypted = forms.ChoiceField(required=True, choices=OPTIONS)
    content = forms.FileField(label="Upload a file here", required=False)


    
    class Meta:
        model = Report
        fields = ( "is_encrypted", "projects"
                  , "sector", "company_name", "company_Phone", "company_location","company_country", "is_private", "content")


#----------------------SignIn/Home-Page----------------------------------

#class SignIn(forms.


#---------------------Make---Group------Form-----------------------------
class GroupForm(forms.Form):
    name = forms.CharField(label='Enter your group name', max_length=100)


    
    class Meta:
        model = Group
