from django.shortcuts import render, redirect
from django.contrib import  messages
from .forms import newmeds
from django.contrib.auth.models import User


# Create your views here.
def meds(request):
    """Return the Ordermeds.html file"""
    if request.method == 'POST':
        form = newmeds(request.POST)
        
        if form.is_valid():
            
            #commits the forignkey (patient) to the db with the for data
            instance = form.save(commit=False)
            instance.patient = request.user
            instance.save()
            
            # needed to display the medicine dose in a message to the customer after commiting
            medicine_name =form.cleaned_data.get('medicine_name')
            dose=form.cleaned_data.get('dose')

            messages.success(request, f'{medicine_name} at {dose} mg order for {User.first_name} {User.last_name}!')
            return redirect('index')
        else:
             form.add_error(None, "There has been an issue with your order. Please try again.")
    form = newmeds()
    
    return render(request, 'ordermeds.html', {'form':form}, )

def addmeds(request):

    """"""
    newmedsform = newmeds(request.POST)

    if newmedsform.is_valid():

        new_meds = newmedsform.save()

    return redirect('index')