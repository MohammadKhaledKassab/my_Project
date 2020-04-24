# -*- coding: utf-8 -*-

from django import forms
#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'write your email', )
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
    
    #Validation #DataFlair
    def clean_password(self):
      password = self.cleaned_data['password']
      if len(password) < 4:
          raise forms.ValidationError("password is too short")
      return password