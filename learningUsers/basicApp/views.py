from django.shortcuts import render
from basicApp import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, "basicApp/index.html")

def register(request):

    registered = False
    if request.method == "POST":
        user_form = forms.userForm(data = request.POST)
        user_profile = forms.userProfileForm(data = request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password) #Hashing the password
            user.save()
            profile = user_profile.save(commit=False)
            profile.user = user #Actualizes the 1-1 relationship
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, user_profile.errors)
    else:
        user_form = forms.userForm()
        user_profile = forms.userProfileForm()

    return render(request, 'basicApp/registration.html', {'user_form':user_form,
                                                           'user_profile':user_profile, 
                                                           'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Django authentication
        user = authenticate(username=username, password=password) 
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Login failed!")
            print("username: {}, password: {}".format(username,password))
            return HttpResponse("Invalid username/password")
    else:
        return render(request, "basicApp/login.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Im secret")