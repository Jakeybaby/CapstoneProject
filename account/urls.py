from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import accpet_job

app_name = 'account'
urlpatterns =[
    path('store/',views.Store,name='store'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cart/',views.cart,name='cart'),
    path('order/',views.Orderlist,name='order'),
    path('order/<int:pk>/',views.OrderDetailView.as_view(),name='orderdetail'),
    path('acceptorder/<int:pk>/', accpet_job, name='accpet_job'),
    path('assigned/', views.Employee_assigned_order, name ='assigned')


    ]