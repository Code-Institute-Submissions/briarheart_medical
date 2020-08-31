from django.urls import path

from . import views

urlpatterns = [
    
    path('success/', views.SuccessView), 
    path('cancelled/', views.CancelledView), 
]