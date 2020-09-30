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
    path('donehiringorder/<int:pk>/', views.employee_hiringorder_job_done, name='employee_hiringorder_job_done'),
    path('declineserviceorder/<int:pk>/', views.decline_ServiceOrder, name='decline_ServiceOrder'),
    path('declinehiringorder/<int:pk>/', views.decline_HiringOrder, name='decline_HiringOrder'),
    path('checkout/', views.checkout, name='checkout'),
    path('admintimesheet/', views.admintimesheet, name='admintimesheet'),
    path('customerOrder/', views.customerOrder, name='customerOrder'),
    path('staffprofile/', views.staffprofile, name='staffprofile'),
    path('customerPreOrder/', views.customerPreOrder, name='customerPreOrder'),
    path('customerprofile/', views.customerprofile, name='customerprofile'),
    path('adminorderlist/', views.adminpage, name='admin_dashboard'),
    path('admindeleteorderlist/<str:pk>/', views.admindeleteorder, name='admindeleteorder'),
    path('admindeletehiringorderlist/<str:pk>/', views.admindeletehiringorder, name='admindeletehiringorder'),
    path('adminOrder/<str:pk>/', views.adminOrder, name='adminOrder'),
    path('adminHiringOrder/<str:pk>/', views.adminHiringOrder, name='adminHiringOrder'),
    path('customerorderfeedback/<str:pk>/', views.customerorderfeedback, name='customerorderfeedback'),
    path('employeeorderfeedback/<str:pk>/', views.employeeorderfeedback, name='employeeorderfeedback'),
    path('payserviceorder/<int:pk>/', views.payserviceorder, name='payserviceorder'),
    path('payhiringorder/<int:pk>/', views.payhiringorder, name='payhiringorder'),
    path('register/', views.CustomerRegiser,name='register'),
    path('staffregister/', views.EmployeeRegiser,name='staffregister'),
    path('logintest/',views.testlogin,name='login'),
    path('staff/',views.staffLogin,name='stafflogin'),
    path('logout/',views.logoutpage,name='logout'),

    path('Employeelist/',views.adminemployeepage,name='adminemployeepage'),
    path('Employeelist/<int:pk>/', views.adminManageEmployee, name='adminManageEmployee'),

    # path('BookJob/',views.BookJob, name='BookJob'),
    path('Contact/',views.contact, name='contact'),
    path('timesheettest/',views.timesheettest, name='timesheettest'),
    path('About/', views.about, name='About'),
    # path('service/', views.servicebook, name='Services'),
    path('service_form/',views.addservicebook_form,name='addservicebook_form'),
    path('pmservice_form/',views.addpmservicebook_form,name='addpmservicebook_form'),
    path('PropertyMaintenance/', views.BookPM, name='PropertyMaintenance'),
    path('HireEquipment/', views.Store, name='HireEquipement'),
    path('adminmanageleave/',views.adminmanageleave, name='adminmanageleave'),
    path('pickuporder/',views.pickuporder, name='pickuporder'),
    # path('Login/', views.login, name='login'),
    # path('PropertyMaintenanced/', views.propertyMaintenance, name='PropertyMaintenance'),


    path('BookPropertyMaintenance/', views.BookPM, name='BookPM'),
    path('BookSecurity/', views.BookSecurity, name='BookSecurity'),
    path('Admin_D/', views.adminpage, name='admin_dashboard'),
    path('Employee_Dash/', views.employeeDashboard, name='employee_dashboard'),
    path('ManagePortal/', views.managePortal, name='managePortal'),
    path('Admin_manageOrders/', views.assignedOrders, name='assignedOrders'),
    path('Employee_Jobs/', views.employeeJobs, name='employeeJobs'),
    path('Timesheet/', views.employeeTimesheet, name='employeeTimesheet'),
    path('timein/', views.timein, name='timein'),
    path('timeout/', views.timeout, name='timeout'),
    path('total/', views.total, name='total'),

]