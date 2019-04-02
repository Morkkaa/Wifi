from django import forms
from .models import *
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


    def clean_password(self):
        new_login = self.cleaned_data['login']
        new_password=self.cleaned_data['password']
        print(self.cleaned_data)

        if User.objects.filter(name=new_login).count():
            pas=User.objects.get(name=new_login)
            print(pas.password)
            if pas.password != new_password:
                raise ValidationError('Wrong password')
            else:
                return new_login
        else:
            raise ValidationError('User dose not exist')








