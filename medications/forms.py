from django import forms
from .models import meds
from django.contrib.auth.models import User



class newmeds(forms.ModelForm):
        
    class Meta:
        model = meds
        doctor = User.objects.filter(is_staff=True)
        fields = ['medicine_name', 'dose', 'address1', 'address2', 'city', 'postcode', 'doctor' ]
        widgets = {
            'medicine': forms.TextInput(attrs={'class':'froms-control', 'placeholder':'Medicine Name', 'aria-label': 'Medicine Name', 'aria-describedby':'add-btn'}),
            'dose' : forms.TextInput(attrs={'class':'froms-control', 'aria-label': 'Dose', 'aria-describedby':'add-btn'}),
            
        }