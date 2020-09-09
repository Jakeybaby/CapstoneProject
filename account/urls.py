from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns =[
    path('',views.index, name='index'),
    # path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('ServiceOrderlist/', views.ServiceOrderlist, name='ServiceOrderlist'),
    path('ServiceOrderlist/<int:pk>/', views.ServiceOrderdetail, name='ServiceOrderdetail'),
    path('HiringOrderlist/', views.HiringOrderlist, name='HiringOrderlist'),
    path('HiringOrderlist/<int:pk>/', views.HiringOrderdetail, name='HiringOrderdetail'),
    path('acceptorder/<int:pk>/', views.accpet_HiringOrder, name='accpet_HiringOrder'),
    path('acceptserviceorder/<int:pk>/', views.accpet_ServiceOrder, name='accpet_ServiceOrder'),
    path('Employee_assigned_order/', views.Employee_assigned_order, name='assigned'),
    path('checkout/', views.checkout, name='checkout'),
    path('customerOrder/', views.customerOrder, name='customerOrder'),


    path('Index/', views.index, name='index'),
    path('BookJob/',views.BookJob, name='BookJob'),
    path('Contact/',views.contact, name='contact'),
    path('security/',views.security, name='Security'),
    path('HireEquipment/', views.Store, name='HireEquipement'),
    path('About/', views.about, name='About'),
    path('service/', views.servicebook, name='ss'),
    path('service_form/',views.addservicebook_form,name='addservicebook_form'),
    path('PropertyMaintenance/', views.servicebook, name='PropertyMaintenance'),


    ]