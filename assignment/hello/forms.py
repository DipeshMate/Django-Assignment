from django import forms 
from .models import Users


class UserForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = ['name','email','role']
    widgets = {
      'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
      'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),
      'role':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Role'}),
    }  
    error_messages ={'name':
      {'required':'Naam likhna bhot jyda zarori hain..!'}
    }
    labels = {'name': 'Name',
              'email':'Email',
              'role':'Role'}
    
    