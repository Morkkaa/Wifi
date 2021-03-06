from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Authorization.as_view(), name='login_url'),
    path('users_list', users_list, name='users_list_url'),
    path('user/create/', UserCreate.as_view(), name='user_create_url'),
    path('users_list/<str:slug>/', users_list_detail, name='user_detail_url'),
]
