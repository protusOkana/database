from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import student

class studentForm(forms.ModelForm):
  class Meta:
      model= student
      fields=['FirstName', 'SecondName','email','regNo','Age']
      class customUser(UserCreationForm):
       class Meta:
          model=User
          fields=['username','password1','password2']
    