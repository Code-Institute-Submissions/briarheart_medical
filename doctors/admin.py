from django.contrib import admin
from django.apps import AppConfig
from .models import doctors
# Register your models here.

class AccountsConfig(AppConfig):
    name = 'doctors'

admin.site.register(doctors)