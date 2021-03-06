"""medi_liver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import index, logout, login, doc_registration, profile, approve_med, decline_med



urlpatterns = [
   
    url(r'^$', index, name="index"),
    
    url(r'^logout/$', logout, name="doc_logout"),
    url(r'^login/$', login, name="doc_login"),
    url(r'^register/$', doc_registration, name="doc_registration"),
    url(r'^profile/$', profile, name="doc_profile"),
 
    
]