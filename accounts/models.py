from django.db import models



  
# Create your models here.
class Patient(models.Model):
    
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    dob = models.DateField(max_length=30)     
    medicine_name = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    username = models.TextField(max_length=30, default='')
    address1 = models.TextField(max_length=30, default='')
    address2 = models.TextField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    postcode = models.CharField(max_length=30, default='')
    username =  models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.title

