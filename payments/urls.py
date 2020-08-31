from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    
    path('success/', views.SuccessView), 
    path('cancelled/', views.CancelledView), 
=======
    path('/home', views.HomePageView.as_view(), name='home'),
>>>>>>> 27185465653bdadd9c4259e549719baed016a333
]