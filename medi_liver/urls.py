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
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
<<<<<<< HEAD

from accounts.views import index
from doctors import urls as urls_doctors
from accounts.views import update_med, delete_med, mark_as_read
from doctors.views import approve_med, decline_med
from django.urls import path
from payments.views import stripe_config, create_checkout_session
=======
from accounts.views import index
from doctors import urls as urls_doctors
from accounts.views import charge, successMsg, payment, update_med, delete_med, mark_as_read
from doctors.views import approve_med, decline_med
from django.urls import path
>>>>>>> 27185465653bdadd9c4259e549719baed016a333




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^doctors/', include(urls_doctors)),
<<<<<<< HEAD
=======
    url(r'^payment/', payment, name="payment"),
    path('charge/', charge, name="charge"),
    path('success/<str:args>/', successMsg, name="success"),
>>>>>>> 27185465653bdadd9c4259e549719baed016a333
    path('update_meds/<str:pk>/', update_med, name="update_med" ),
    path('delete_meds/<str:pk>/', delete_med, name="delete_med" ),
    path('approve/<str:pk>/', approve_med, name="approve_med"),
    path('decline/<str:pk>/', decline_med, name="decline_med"),
    path('mark_as_read/<str:pk>/', mark_as_read, name="mark_as_read"),
    path('', include('payments.urls')),
<<<<<<< HEAD
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
=======
>>>>>>> 27185465653bdadd9c4259e549719baed016a333
]