from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def events(request):
    return render(request, 'events.html',{})

def gallery(request):
    return render(request, 'gallery.html',{})
 
#@login_required(redirect_field_name='loginpage')
def index(request):
    return render(request, 'index.html',{})

def home(request):
    return render(request,'home.html',{})
    
def maps(request):
    return render(request,'map.html',{})

def mapsd(request):
    return render(request,'3dmap.html',{})

def loginpage(request):
    return render(request,'login.html',{})

def loginvalidate(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(username = user, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            error_message = 'invalid credentials'
            return render(request,'error.html',{'error_message':error_message})
    else:
        error_message = 'This is not a valid request'
        return render(request,'error.html',{'error_message':error_message})


def signin(request):
    pass

def signup(request):
     return render(request, 'registration.html',{})

def social(request):
    return render(request, 'social.html',{})

def sponsors(request):
    return render(request, 'sponsors.html',{})

def team(request):
    return render(request, 'team.html',{})