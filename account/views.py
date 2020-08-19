from django.shortcuts import render
from django.http import HttpResponse
from .form import UserRegisterForm
from .models import *
from Oneshop.models import *
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'account/Index.html')

def BookJob(request):
    return render(request, 'account/BookJob.html')


def Cusinfo(request):
    customer = request.user.customerprofile
    order=Order.objects.get(cus_order=customer)
    equipment = order.cartitem_set.all()
    propetyservice = order.propertyorder_set.all()
    securityservice = order.securityorder_set.all()

    userorder = request.user.customerprofile.order_set.all()
    context = {

        'userorder':userorder,
        'eq':equipment,
        'propetyservice':propetyservice,
        'securityservice':securityservice

    }
    return render(request, 'account/test.html', context)


def CustomerRegiser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("ok")

    else:
        form = UserRegisterForm()
        print('not ok')

    context = {'form': form}
    return render(request, 'account/userregister.html', context)


def Store(request):
    equipment = Equipment.objects.all()

    context = {
        "equipment": equipment
    }
    return render(request, 'account/store.html', context)


def cart(request):
    customer = request.user.customerprofile
    order, created = Order.objects.get_or_create(cus_order=customer, complete=False)
    equipment = order.cartitem_set.all()
    context = {
        'equipment': equipment,
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

    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1)
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)

    cartItem.save()
    if cartItem.quantity <= 0:
        cartItem.delete()

    return JsonResponse('Item added', safe=False)
