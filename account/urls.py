from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[

    path('rege/',views.CustomerRegiser,name='register'),
    path('usinfo/',views.Cusinfo,name='register')
]