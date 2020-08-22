from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class doctors(models.Model):
    
    title = models.CharField(max_length=4)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    
    def __str__(self):
        return (self)