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


        if User.objects.filter(name=new_login).count():
            pas=User.objects.get(name=new_login)

            if pas.password != new_password:
                raise ValidationError('Wrong password')
            else:
                return new_login
        else:
            raise ValidationError('User dose not exist')



class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['name', 'slug', 'password', 'access_time']

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'access_time': forms.TextInput(attrs={'class': 'form-control'})
        }
    def clean_slug(self):
        new_slug=self.cleaned_data['slug'].lower()

        if new_slug=='create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug








