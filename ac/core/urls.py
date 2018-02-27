from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('maps/',views.maps, name = 'maps'),
    path('signin/', views.signin , name = 'sigin'),
    path('sponsers/', views.sponsers , name = 'sponsers'),
    path('team/', views.team , name = 'team'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('social/', views.social, name = 'social'),
    path('events/', views.events , name = 'events'),

]
