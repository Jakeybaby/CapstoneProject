from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import accpet_job

app_name = 'account'

urlpatterns =[
    path('',views.index, name='index'),
    # path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('order/', views.Orderlist, name='order'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='orderdetail'),
    path('acceptorder/<int:pk>/', accpet_job, name='accpet_job'),
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