from django.urls import path, include
from . import views

urlpatterns= [ 
    path('reg/',views.first_task, name = 'task_name'),
]
