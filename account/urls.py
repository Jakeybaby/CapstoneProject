from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[

    path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('',views.index),
    path('Index', views.index, name='index'),
    path('BookJob',views.BookJob, name='BookJob'),
    path('Contact',views.BookJob, name='contact'),
    path('security',views.BookJob, name='security'),
    path('PropertyMaintenance', views.propertyMaintenance, name='PropertyMaintenance'),
    path('HireEquipment', views.HireEquipment, name='HireEquipment'),
    path('About', views.about, name='About')

    ]