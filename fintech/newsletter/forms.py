# importing forms
from django import forms
from django.contrib.auth.models import User

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