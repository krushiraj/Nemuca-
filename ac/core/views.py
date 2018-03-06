from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

 Create your views here.
@login_required(redirect_field_name='loginpage')
def events(request):
    return render(request, 'eventre.html',{})

@login_required(redirect_field_name='loginpage')
def gallery(request):
    return render(request, 'gallery.html',{})

@login_required(redirect_field_name='loginpage')
def index(request):
    return render(request, 'index.html',{})

@login_required(redirect_field_name='loginpage')
def home(request):
    return render(request,'home.html',{})

@login_required(redirect_field_name='loginpage')
def maps(request):
    return render(request,'map.html',{})

@login_required(redirect_field_name='loginpage')
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

@login_required(redirect_field_name='loginpage')
def signup(request):
     return render(request, 'registration.html',{})

@login_required(redirect_field_name='loginpage')
def social(request):
    return render(request, 'social.html',{})

@login_required(redirect_field_name='loginpage')
def sponsors(request):
    return render(request, 'sponsors.html',{})

@login_required(redirect_field_name='loginpage')
def team(request):
    return render(request, 'team.html',{})

def secret(request):
    return render(request,'ll.html' ,{})