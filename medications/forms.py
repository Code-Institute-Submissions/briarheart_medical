from django import forms
from .models import meds



class newmeds(forms.ModelForm):
    class Meta:
        model = meds
        fields = ['medicine_name', 'dose', 'address1', 'address2', 'city', 'postcode' ]
        widgets = {
            'medicine': forms.TextInput(attrs={'class':'froms-control', 'placeholder':'Medicine Name', 'aria-label': 'Medicine Name', 'aria-describedby':'add-btn'}),
            'dose' : forms.TextInput(attrs={'class':'froms-control', 'aria-label': 'Dose', 'aria-describedby':'add-btn'}),
            
        }