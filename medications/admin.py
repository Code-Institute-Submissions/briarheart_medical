from django.contrib import admin
from django.apps import AppConfig
from .models import meds
# Register your models here.

class AccountsConfig(AppConfig):
    name = 'medicines'

admin.site.register(meds)