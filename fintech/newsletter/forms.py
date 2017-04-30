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
    GROUPS_CHOICE = ()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ReportForm, self).__init__(*args, **kwargs)
        self.GROUPS_CHOICE = self.GROUPS_CHOICE + (('None', 'None'),)
        for group in Group.objects.all():
            if user in group.user_set.all():
                self.GROUPS_CHOICE = self.GROUPS_CHOICE + ((group.name, group.name),)
        self.fields['group'].choices = self.GROUPS_CHOICE



    company_name = forms.CharField(required=True, label="Enter Company Name")
    industry = forms.CharField(required=True, label="Enter Industry")
    company_Phone = forms.CharField(required=True, label="Enter Company Phone Number")
    company_location = forms.CharField(required=True, label="Enter Company Location")
    company_country = forms.ChoiceField(required=True, choices=COUNTRIES, label="Enter Company Country")
    sector = forms.CharField(required=True, label="Enter Company Sector")
    ceo_name = forms.CharField(required=True, label="Enter CEO name")
    #group = forms.CharField(required=False, label="What group can view this?")
    group = forms.ChoiceField(label="Which Group Should This Report Be Associated With?", required=True,
                              choices=GROUPS_CHOICE)

    industry = forms.CharField(required=True, label="Enter Industry")

    is_private = forms.ChoiceField(label="Is This Private?", required=True, choices=OPTIONS)
    projects = forms.CharField(required=True, label="Enter Project Name(s) Separated by Commas")
    is_encrypted = forms.ChoiceField(label="Is The File Encrypted?",required=True, choices=OPTIONS)
    content = forms.FileField(label="Upload a file here",
                              widget=forms.FileInput(attrs={'multiple': True, 'type': 'file', 'class' : 'button'}), required=False) #'onchange':'getName'


    
    class Meta:
        model = Report
        fields = ("projects" ,"industry", "company_name", "sector","ceo_name", "company_Phone", "company_location",
                  "company_country", "is_private", "content", "is_encrypted")

#----------------------SignIn/Home-Page----------------------------------

#class SignIn(forms.


#---------------------Make---Group------Form----------------------------- 
class GroupForm(forms.Form):
    name = forms.CharField(label='Enter your group name', max_length=22)

    class Meta:
        model = Group
        fields = ('name',)
#------------------------FILE ADD FORM -----------------------------------
class FileAddForm(forms.Form):
    content = forms.FileField(label="Upload a file here",
                              widget=forms.FileInput(attrs={'multiple': True, 'type': 'file', 'class': 'button'}),
                              required=False)
    class Meta:
        model = Report
        fields = ("content",)
