from django.contrib import admin
from .models import *

class AddUser(admin.ModelAdmin):
    list_display = ('name', 'password', 'data', 'access_time')

admin.site.register(User, AddUser)

