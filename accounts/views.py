from django.shortcuts import render, redirect, reverse, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from accounts.forms import UserLoginForm, UserRegistrationForm
from medications.models import meds
from medications.forms import newmeds

<<<<<<< HEAD
=======
import stripe
import os
import env

stripe.api_key = os.environ.get('STRIPE_SECRET')


>>>>>>> 27185465653bdadd9c4259e549719baed016a333

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
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


<<<<<<< HEAD
=======
def charge(request):
        amount = 5
        if request.method == "POST":
            print('Data' , request.POST)
        
        session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': '{{prod_Hv4AiNmlXYlbih}}',
            'quantity': 1,
        }],
        mode='subscription',
        success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://example.com/cancel',
)

        return redirect(reverse('success', args = [amount]))

def successMsg(request, args):
    _id=request.user.id
    obj = meds.objects.filter(patient=_id)

    amount = args
    return render(request, 'success.html', {'amount': amount, 'obj':obj})

def payment(request):
    """Return the paymets.html file"""
    return render(request,  'payment.html')

>>>>>>> 27185465653bdadd9c4259e549719baed016a333
#   CRUD

#CREATE

def registration(request):
    """Render the registration page"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')

           
            messages.success(request, f'Account Created for {first_name} {last_name}!')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form':form})

#READ
def profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    _id=request.user.id
    obj = meds.objects.filter(patient=_id)
    
    print(_id)

    return render(request, 'profile.html', {"profile": user, "obj":obj} )

#UPDATE
def update_med(request, pk):
    """Return the updatemeds.html file"""
    
    order = meds.objects.get(id=pk)
    form = newmeds(instance=order, user=request.user)

    if request.method == 'POST':
        form=newmeds(request.POST, instance=order, user=request.user)
        if form.is_valid():            
            form.save()
            return redirect('index')
    

    return render(request, 'updatemeds.html', {'form':form} )


#DELETE

def delete_med(request, pk):
    """Return the updatemeds.html file"""
    
    order = meds.objects.get(id=pk)
    if request.method == "POST":
		    order.delete()
		    return redirect('profile')
    

    return render(request, 'delete.html', {'item':order} )


def mark_as_read(request, pk):
    """update meds model to mark as read"""
    
    order = meds.objects.get(id=pk)
   

    if request.method == "POST":
        order.read = True
        order.save()
        return redirect('profile')
    
    return render(request, 'confirmation.html', {'item':order})

<<<<<<< HEAD
def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')
=======
>>>>>>> 27185465653bdadd9c4259e549719baed016a333
