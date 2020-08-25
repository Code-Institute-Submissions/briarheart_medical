from django.db import models
from doctors.models import doctors
from django.contrib.auth.models import User
# Create your models here.

class meds(models.Model):
    medicine_name = models.CharField(max_length=45)
    dose = models.CharField(max_length=3)
    patient = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    postcode = models.CharField(max_length=8)
    doctor = models.ForeignKey(User, related_name="+", on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return '{} {} {} {} {}'.format(self.medicine_name, self.dose, self.patient, self.city, self.postcode)

