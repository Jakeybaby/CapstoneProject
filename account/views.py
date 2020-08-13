from django.shortcuts import render
from django.http import HttpResponse
from .form import UserRegisterForm
from .models import *
from Oneshop.models import *

# Create your views here.
def CustomerLogin(request):
    pass

def Cusinfo(request):

    os = Order.objects.all()
    dd = request.user.customerprofile.order_set.all()
    eqorder = EquiementOrder.objects.all()
    context = {

        'order':os,
        'test':dd,
        'eqo':eqorder

    }
    return render(request,'account/UserProfile.html',context)


def CustomerRegiser(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("ok")

    else:
        form = UserRegisterForm()
        print('not ok')

    context = {'form':form}
    return render(request,'account/userregister.html',context)