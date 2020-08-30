from django import forms
from .models import meds
from django.contrib.auth.models import User



class newmeds(forms.ModelForm):
        
    class Meta:
        model = meds
        
        fields = ['medicine_name', 'dose', 'address1', 'address2', 'city', 'postcode', 'doctor' ]
        widgets = {
            'medicine': forms.TextInput(attrs={'class':'froms-control', 'placeholder':'Medicine Name', 'aria-label': 'Medicine Name', 'aria-describedby':'add-btn'}),
            'dose' : forms.TextInput(attrs={'class':'froms-control', 'aria-label': 'Dose', 'aria-describedby':'add-btn'}),
            
        }

    #filters the docs from the patients from the Auth_User table
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(newmeds, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(is_staff=True)

    
    def formfield_for_foreignkey(self, anything, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        
        return super().formfield_for_foreignkey(anything, request, using=self.using, **kwargs)
        