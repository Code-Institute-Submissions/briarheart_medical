from django.shortcuts import render, redirect, reverse, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from doctors.forms import UserLoginForm, DocRegistrationForm
from medications.models import meds


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                if user.is_staff:
                    messages.success(request, "You have successfully logged in!")
                    return redirect(reverse('index'))
                else:
                    return redirect(reverse('correction'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'doc_login.html', {'login_form': login_form})


def doc_registration(request):
    """Render the Doctor registration page"""
    if request.method == 'POST':
        doc_form = DocRegistrationForm(request.POST)
        if doc_form.is_valid():            
            doc_form.save()
            first_name=doc_form.cleaned_data.get('first_name')
            last_name=doc_form.cleaned_data.get('last_name')
            title=doc_form.cleaned_data.get('title')

           
            messages.success(request, f'Account Created for {title}. {first_name} {last_name}!')
            return redirect('index')
    else:
        doc_form = DocRegistrationForm()
    return render(request, 'doc_registration.html', {'doc_form':doc_form})

def profile(request):
    """The Doctor's profile page"""
    user = User.objects.get(email=request.user.email)
    _id=request.user.id
    obj = meds.objects.filter(doctor=_id)
    return render(request, 'doc_profile.html', {"profile": user, "obj":obj})

#UPDATE
def approve_med(request, pk):
    """update meds model to approve order"""
    
    order = meds.objects.get(id=pk)
    patient = order.patient
    if request.method == "POST":
        order.declined = False
        order.actioned = True
        order.approved = True
        order.save()
        return redirect('doc_profile')
    
    return render(request, 'approve.html',  {'item':order, "patient":patient} )

#UPDATE
def decline_med(request, pk):
    """update meds model to decline order order"""
    
    order = meds.objects.get(id=pk)
    patient = order.patient

    if request.method == "POST":
        order.approved = False
        order.actioned = True
        order.decline = True
        order.save()
        return redirect('doc_profile')
    
    return render(request, 'decline.html', {'item':order, "patient":patient} )