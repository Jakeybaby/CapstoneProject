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
    path('adminorderlist/', views.adminpage, name='admin_dashboard'),
    path('adminOrder/<str:pk>/', views.adminOrder, name='adminOrder'),
    path('customerorderfeedback/<str:pk>/', views.customerorderfeedback, name='customerorderfeedback'),
    path('employeeorderfeedback/<str:pk>/', views.employeeorderfeedback, name='employeeorderfeedback'),


    path('register/', views.CustomerRegiser,name='register'),
    path('staffregister/', views.EmployeeRegiser,name='staffregister'),
    path('logintest/',views.testlogin,name='login'),
    path('staff/',views.staffLogin,name='stafflogin'),
    path('logout/',views.logoutpage,name='logout'),
    path('wtf/',views.adminemployeepage,name='adminemployeepage'),


    path('BookJob/',views.BookJob, name='BookJob'),
    path('Contact/',views.contact, name='contact'),
    path('security/',views.security, name='Security'),
    path('About/', views.about, name='About'),
    path('service/', views.servicebook, name='ss'),
    path('service_form/',views.addservicebook_form,name='addservicebook_form'),
    path('PropertyMaintenance/', views.servicebook, name='PropertyMaintenance'),
    path('Security/',views.Security, name='security'),
    path('HireEquipment/', views.Store, name='HireEquipement'),
    # path('Login/', views.login, name='login'),
    path('Services/', views.Services, name='Services'),
    path('PropertyMaintenance/', views.propertyMaintenance, name='PropertyMaintenance'),


    path('BookPropertyMaintenance/', views.BookPM, name='BookPM'),
    path('BookSecurity/', views.BookSecurity, name='BookSecurity'),
    path('Admin_D/', views.Admin_D, name='admin_dashboard'),
    path('Employee_Dash/', views.employeeDashboard, name='employee_dashboard'),
    path('ManagePortal/', views.managePortal, name='managePortal'),
    path('Admin_manageOrders/', views.assignedOrders, name='assignedOrders'),
    path('Employee_Jobs/', views.employeeJobs, name='employeeJobs'),
    path('Timesheet/', views.employeeTimesheet, name='employeeTimesheet'),



    ]