from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/',views.home,name = 'home'),
    path('maps/',views.maps, name = 'maps'),
    path('maps/3dmap',views.mapsd, name = 'mapsd'),
    path('accounts/login/', views.loginpage , name = 'loginpage'),
    path('login/validate', views.loginvalidate , name = 'loginvalidate'),
    path('sponsors/', views.sponsors , name = 'sponsors'),
    path('team/', views.team , name = 'team'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('social/', views.social, name = 'social'),
    path('events/', views.events , name = 'events'),
    path('signup/', views.signup , name = 'signup'),   
]