from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from .form import UserRegisterForm
from .models import *
from Oneshop.models import *
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'account/Index.html')


def about(request):
    return render(request, 'account/About.html')

def BookJob(request):
    return render(request, 'account/BookJob.html')

def HireEquipment(request):
    return render(request, 'account/preHire.html')

def contact(request):
        return render(request, 'account/Contact.html')

def security(request):
    return render(request, 'account/security.html')


def propertyMaintenance(request):
    return render(request, 'account/PropertyMaintenance.html')




def Employee_assigned_order(request):

    staff = request.user.employeeprofile
    assigned_order = staff.order_set.all()

    context = {
        'order':assigned_order
    }

    return render(request,'account/assigned.html',context)


def Orderdetail(request,id):

    ins = get_object_or_404(Order, id=id)
    context = {
        'orderdetail': ins
    }
    return render(request, 'account/orderdetail.html', context)


class OrderDetailView(DetailView):
    model = Order
    template_name = "account/orderdetail.html"

def Orderlist(request):

    order = Order.objects.all()
    context = {
        'orders': order
    }
    return render(request, 'account/orderlist.html', context)


def accpet_job(request,pk):

    ins = get_object_or_404(Order, pk=pk)
    ins.employee_order = request.user.employeeprofile
    ins.assigned = True
    ins.save()

    return redirect('account:order')


def checkout(request):

    customer = request.user.customerprofile
    order = get_object_or_404(Order, cus_order=customer,complete=False)
    order.complete = True
    order.isHiring = True
    order.save()
    return redirect('account:HireEquipement')


#
# def CustomerRegiser(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = UserRegisterForm()
#
#     context = {'form': form}
#     return render(request, 'account/userregister.html', context)


def Store(request):
    products = Equipment.objects.all()
    customer = request.user.customerprofile
    order, created = Order.objects.get_or_create(cus_order=customer, complete=False)
    equipment = order.cartitem_set.all()
    context = {
        "products": products,
        'equipments': equipment,
        'order': order,
    }
    return render(request, 'account/HireEquipement.html', context)


def cart(request):
    customer = request.user.customerprofile
    order, created = Order.objects.get_or_create(cus_order=customer,complete=False)
    equipment = order.cartitem_set.all()
    context = {
        'equipments': equipment,
        'order':order,
    }
    return render(request, 'account/cart.html', context)


def updateItem(request):

    data = json.loads(request.body)
    equipmentID = data['equipmentID']
    action = data['action']

    customer = request.user.customerprofile
    equipment = Equipment.objects.get(id=equipmentID)
    order, created = Order.objects.get_or_create(cus_order=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(order=order, equipment=equipment)
    # cartItem, created = CartItem.objects.get_or_create(equipment=equipment)

    if action == 'add':
        if equipment.stock <= 0:
            print('not enough stocking')
        else:
            cartItem.quantity = (cartItem.quantity + 1)
            cartItem.save()

    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)
        cartItem.save()
    elif action == 'delete':
        cartItem.delete()


    if cartItem.quantity <= 0:
        cartItem.delete()

    return JsonResponse('Item added', safe=False)





def servicebook(request):
    services = SecurityServices.objects.all()
    context ={
        'services':services
    }
    return render(request,'account/servicebooking.html',context)

def addservicebook_form(request):

    service_id = request.POST['servicename']
    service_notes = request.POST['description']
    service_date = request.POST['servicedate']
    service_user = request.user.customerprofile
    service_name = SecurityServices.objects.get(id=service_id)

    order = Order.objects.create(cus_order=service_user, complete=True, isService=True)
    securityorder, created = SecurityOrder.objects.get_or_create(order=order, security_service=service_name, description=service_notes, date_required=service_date)

    securityorder.save()
    return render(request,'account/servicebooking.html')

def customerOrder(request):

    customer = request.user.customerprofile
    order = Order.objects.filter(cus_order=customer)
    context={
        'orders':order
    }
    return render(request,'account/UserPage.html',context)