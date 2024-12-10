from django import forms 
from .models import Users


class UserForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = ['name','email','role']
    widgets = {
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
      'role':forms.TextInput(attrs={'class':'form-control'}),
    }  