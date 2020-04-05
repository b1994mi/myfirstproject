from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import transaction
from datetime import datetime

from .forms import ProfileForm, UserForm
from .models import Profile, Logger


# Put some common url path into variable to reduce hardcoding the path.
userprofileurl  = "mymapapp/userprofile.html"
mapurl          = "mymapapp/map.html"
loginurl        = "mymapapp/login.html"
signupurl       = "mymapapp/signup.html"


"""
There are 5 view methods:
- Home view shows User Profile page if logged in and redirects to log in page if not,
- Sign Up and Log In views to give a sign up form and log in form respectively,
- Log Out view that only calls the logout() method and redirects to Home,
- Map view queries the Profile Model (or table) where lon and lat field is not null.

Note:
I have implemented a user log in/out activity logger inside login_view and logout_view method.
If user log in, the logb field is True; False for user log out. 
"""


@transaction.atomic
def home_view(request):

    # Current logged in user is assigned into currentUser variable.
    currentUser = request.user

    # If currentUser not logged in handling.
    if not currentUser.is_authenticated:
        return redirect('mymapapp:login')

    # Find the record of current logged in user in Profile table using primary key.
    prof = Profile.objects.select_related('user').get(pk = currentUser.profile.pk)

    # Save the User Model Form and Profile Model Form form user input.
    if request.method == "POST":
        user_form = UserForm(request.POST, instance = currentUser)
        profile_form = ProfileForm(request.POST, instance = prof)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            messages.error(request, 'You entered the form incorrectly.')

    # The User Form instance provided by Django is assigned into user_form variable.
    user_form = UserForm(instance = currentUser)
    profile_form = ProfileForm(instance = prof)

    # Render the page with those two forms above and prof object/query.
    return render(request, userprofileurl, {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'prof' : prof,
    })


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success, you made a User.')
        else:
            messages.error(request, 'You entered the form incorrectly.')

    return render(request, signupurl, {'form': UserCreationForm()})


def login_view(request):
    # User is logged in handling.
    if request.user.is_authenticated:
        return redirect('mymapapp:home')

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())

            # Save last_login from User Model & create a new record in Logger Model.
            l = Logger(user = request.user, logb = True, tlog = request.user.last_login)
            l.save()

            return redirect('mymapapp:home')
        else:
            messages.error(request, 'You entered the wrong username or password.')

    return render(request, loginurl, {'form': AuthenticationForm()})  


def logout_view(request):
    # If logged in or request method is post, log the user out.
    if request.user.is_authenticated or request.method == 'POST':
        
        # Save current time and create a new record in Logger Model.
        l = Logger(user = request.user, logb = False, tlog = datetime.now())
        l.save()
        
        logout(request)

    # Whether the user is logged in or not, redirect to home.
    return redirect('mymapapp:home')


def map_view(request):
    # User not logged in handling.
    if not request.user.is_authenticated:
        return redirect('mymapapp:login')

    # Only query the records form Profile table that have longitude and latitude,
    # INNER JOIN those tables using select_related method.
    data = Profile.objects.exclude(lngd__isnull=True, latd__isnull=True).select_related('user')
    return render(request, mapurl, {'profiles': data})