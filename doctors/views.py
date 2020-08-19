from django.shortcuts import render, redirect, reverse, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from doctors.forms import UserLoginForm, UserRegistrationForm





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


def registration(request):
    """Render the registration page"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.is_staff = True
            form.save()
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')

           
            messages.success(request, f'Account Created for Dr. {first_name} {last_name}!')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'doc_registration.html', {'form':form})

def profile(request):
    """The Doctor's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'doc_profile.html', {"profile": user})

