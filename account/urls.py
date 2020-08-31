from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import accpet_job

app_name = 'account'

urlpatterns =[
    path('',views.index, name='index'),
    path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('order/', views.Orderlist, name='order'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='orderdetail'),
    path('acceptorder/<int:pk>/', accpet_job, name='accpet_job'),
    path('assigned/', views.Employee_assigned_order, name='assigned'),
    path('Index', views.index, name='index'),
    path('BookJob',views.BookJob, name='BookJob'),
    path('Contact',views.contact, name='contact'),
    path('security',views.security, name='Security'),
    path('HireEquipement', views.HireEquipement, name='HireEquipement'),
    path('PropertyMaintenance', views.propertyMaintenance, name='PropertyMaintenance'),
    path('About', views.about, name='About')

    ]