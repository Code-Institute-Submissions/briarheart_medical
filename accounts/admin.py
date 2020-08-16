from django.apps import AppConfig
from django.contrib import admin
from .models import Patient


class AccountsConfig(AppConfig):
    name = 'accounts'

admin.site.register(Patient)