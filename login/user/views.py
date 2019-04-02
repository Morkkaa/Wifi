from django.shortcuts import render
from .models import *
from django.views.generic import View
from .forms import *
from django.http import HttpResponse


class Authorization(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'user_auth.html', context={'form': form})

    def post(self, request):
        bound_form=LoginForm(request.POST)
        if bound_form.is_valid():
            return HttpResponse('Вход выполнен')
        return render(request, 'user_auth.html', context={'form':bound_form})

#def authorization(request):
#    return render(request, 'user_auth.html')

def users_list(request):
    users=User.objects.all()
    return render(request, 'Users_list.html', context={'users': users})

def users_list_detail(request, slug):
    user=User.objects.get(slug__iexact=slug)
    return render(request, 'user_detail.html', context={'user':user, 'slug':slug})

