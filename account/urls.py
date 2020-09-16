from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns =[
    path('',views.index, name='index'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('ServiceOrderlist/', views.ServiceOrderlist, name='ServiceOrderlist'),
    path('ServiceOrderlist/<int:pk>/', views.ServiceOrderdetail, name='ServiceOrderdetail'),
    path('HiringOrderlist/', views.HiringOrderlist, name='HiringOrderlist'),
    path('HiringOrderlist/<int:pk>/', views.HiringOrderdetail, name='HiringOrderdetail'),
    path('acceptorder/<int:pk>/', views.accpet_HiringOrder, name='accpet_HiringOrder'),
    path('acceptserviceorder/<int:pk>/', views.accpet_ServiceOrder, name='accpet_ServiceOrder'),
    path('doneorder/<int:pk>/', views.employee_order_job_done, name='employee_order_job_done'),
    path('declineserviceorder/<int:pk>/', views.decline_ServiceOrder, name='decline_ServiceOrder'),
    path('checkout/', views.checkout, name='checkout'),
    path('customerOrder/', views.customerOrder, name='customerOrder'),
    path('adminorderlist/', views.adminpage, name='adminpage'),
    path('adminOrder/<str:pk>/', views.adminOrder, name='adminOrder'),
    path('customerorderfeedback/<str:pk>/', views.customerorderfeedback, name='customerorderfeedback'),
    path('employeeorderfeedback/<str:pk>/', views.employeeorderfeedback, name='employeeorderfeedback'),


    path('BookJob/',views.BookJob, name='BookJob'),
    path('Contact/',views.contact, name='contact'),
    path('security/',views.security, name='Security'),
    path('About/', views.about, name='About'),
    path('service/', views.servicebook, name='ss'),
    path('service_form/',views.addservicebook_form,name='addservicebook_form'),
    path('PropertyMaintenance/', views.servicebook, name='PropertyMaintenance'),
    path('Security/',views.Security, name='security'),
    path('HireEquipment/', views.Store, name='HireEquipement'),
    path('Login/', views.login, name='login'),
    path('Services/', views.Services, name='Services'),
    path('PropertyMaintenance/', views.propertyMaintenance, name='PropertyMaintenance'),



    ]