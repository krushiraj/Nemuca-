from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request, 'events.html',{})

def gallery(request):
    return render(request, 'gallery.html',{})
 
def index(request):
    return render(request, 'index.html',{})

def maps(request):
    return render(request,'map.html',{})

def mapsd(request):
    return render(request,'3dmap.html',{})

def login(request):
    return render(request, 'registration.html', {})

def signin(request):
    pass

def signup(request):
    pass

def social(request):
    return render(request, 'social.html',{})

def sponsors(request):
    return render(request, 'sponsors.html',{})

def team(request):
    return render(request, 'team.html',{})