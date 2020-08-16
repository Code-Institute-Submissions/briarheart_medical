from django import forms
from .models import Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import datetime



class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterform(UserCreationForm):
    TITLE_CHOICES = [
    ('', 'Please Choose'),
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]
    
    email = forms.EmailField()
    username = forms.CharField(label="Username") 
    title = forms.ChoiceField(choices=TITLE_CHOICES, label="Title")
    first_name = forms.CharField(label="First Name") 
    last_name = forms.CharField(label="Surname")
    dob = forms.DateField(initial="dd/mm/yyyy", label="Date of Birth") 
    medicine_name = forms.CharField(label="Name Of medicine")
    address1 = forms.CharField(label="Address")
    address2 = forms.CharField(label="")
    city = forms.CharField(label="City")
    postcode = forms.CharField(label="Postcode")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['title','first_name', 'last_name', 'dob', 'email', 'username', 'password1', 'password2', 'medicine_name','address1', 'address2', 'city', 'postcode']

"""
class UserRegistrationForm(forms.ModelForm):
   #Form used to register a new user
   
    MEDICINE_CHOICES = [
    ('', 'Please Choose'),
    ('SPRAY', 'Spray.'),
    ('CREAM/GEL', 'Cream or Gel.'),
    ('TABLET', 'Tablet.'),
]


    title = forms.ChoiceField(choices=TITLE_CHOICES, label="Title")
    first_name = forms.CharField(label="First Name") 
    last_name = forms.CharField(label="Surname")
    dob = forms.DateField(initial="dd/mm/yyyy", label="Date of Birth") 
    medicines = forms.ChoiceField(choices=MEDICINE_CHOICES, label="Medicines to order") 
    medicine_name = forms.CharField(label="Name Of medicine")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    dose = forms.DecimalField(label="Dose in mg" )
        
                                                  
    
    class Meta:
        model = Patient
        fields = ['title','first_name', 'last_name', 'dob', 'email', 'username', 'password1', 'password2', 'medicines']

def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2

    """


