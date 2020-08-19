from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[

    path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('',views.index),
    path('BookJob.html/',views.BookJob)


    ]