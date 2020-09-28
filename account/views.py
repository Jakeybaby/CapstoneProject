from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from .form import UserRegisterForm
from .models import *
from Oneshop.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .form import *
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
from django.core.mail import send_mail
import json


def index(request):

    return render(request, 'account/Index.html')


def about(request):
    return render(request, 'account/AboutUs.html')



def contact(request):
    return render(request, 'account/Contact.html')



# --

def admintimesheet(request):
    return render(request,'account/admintimesheet.html')

# book a security service function
@login_required(login_url='account:login')
def addservicebook_form(request):
    service_id = request.POST['servicename']
    service_notes = request.POST['description']

    service_date = request.POST['servicedate']

    service_user = request.user.customerprofile
    service_name = SecurityServices.objects.get(id=service_id)
    service_address = request.POST['address']
    service_geo = request.POST['geolocation']
    service_fullname = request.POST['fullname']
    service_phone = request.POST['service_phone']

    order = Order.objects.create(cus_order=service_user, complete=True, isService=True, server_date=service_date,
                                 address=service_address, geolocation=service_geo,fullName=service_fullname,phoneNumber=service_phone)
    securityorder, created = SecurityOrder.objects.get_or_create(order=order, security_service=service_name,
                                                                 notes=service_notes, date_required=service_date)

    securityorder.save()
    messages.success(request,'Success book order :'+ str(order.id))
    return redirect('account:customerOrder')


@login_required(login_url='account:login')
def addpmservicebook_form(request):
    service_id = request.POST['servicename']
    service_notes = request.POST['description']
    service_date = request.POST['servicedate']
    service_user = request.user.customerprofile
    service_name = PropetyServices.objects.get(id=service_id)
    service_address = request.POST['address']
    service_geo = request.POST['geolocation']
    service_fullname = request.POST['fullname']
    service_phone = request.POST['service_phone']

    order = Order.objects.create(cus_order=service_user, complete=True, isService=True, server_date=service_date,
                                 address=service_address, geolocation=service_geo,fullName=service_fullname,phoneNumber=service_phone)
    propertyorder, created = PropertyOrder.objects.get_or_create(order=order, property_service=service_name,
                                                                 notes=service_notes, date_required=service_date)

    propertyorder.save()
    messages.success(request,'Success book order :'+ str(order.id))
    return redirect('account:customerOrder')



def BookPM(request):

    services = PropetyServices.objects.all()
    form = servicebook_form()
    context = {
        'services':services,
        "form": form
    }

    return render(request, 'account/BookPropertyMaintenance.html',context)


def BookSecurity(request):

    services = SecurityServices.objects.all()
    form = servicebook_form()
    context = {
        'services': services,
        'form': form
    }
    return render(request, 'account/BookSecurity.html',context)





def assignedOrders(request):

    order = Order.objects.all()
    hiringorder = HiringOrder.objects.all()
    context = {
        'object': order,
        'hiringorders':hiringorder
    }
    return render(request, 'account/Admin_manageOrders.html',context)


def managePortal(request):
    return render(request, 'account/ManagePortal.html')


@login_required(login_url='account:stafflogin')
def adminpage(request):
    order = Order.objects.all()
    hiringorder = HiringOrder.objects.all()
    context = {
        'object': order,
        'hiringorders':hiringorder
    }
    return render(request, 'account/Admin_D.html', context)

def adminemployeepage(request):
    memeber = EmployeeProfile.objects.all()

    context = {'member':memeber}
    return render(request,'account/adminemployeepage.html',context)


# to see the detail of each order
def adminOrder(request, pk):
    order = Order.objects.get(id=pk)
    num = order.id
    form = adminform(instance=order)
    form.fields['employee_order'].choices = list()
    for k in GroupEmployee.objects.all():
        # Append the tuple of OptGroup Name, Organism.
        form.fields['employee_order'].choices.append(
            (

                k.name,  # First tuple part is the optgroup name/label
                list(  # Second tuple part is a list of tuples for each option.
                    (o.id, o.employee_user.first_name) for o in EmployeeProfile.objects.filter(group=k).order_by('employee_user')
                    # Each option itself is a tuple of id and name for the label.
                )
            )
        )

    if request.method == 'POST':
        form = adminform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # sending notification when assign the job to employee
            em = order.employee_order.employee_user.email
            subject = order.address
            jobdate = order.server_date
            send_mail(
                'New Job Request',
                'You have a New Order Request to' + str(subject) + ' on ' + str(jobdate) + '\n' +'Please Login in to Your Account to Confirm it',
                'dcf1996028@gmail.com',
                [em],
                fail_silently=False,
            )
            messages.success(request, 'Order '+str(num)+' has been assgined')
            return redirect('account:admin_dashboard')

    context = {'form': form}
    return render(request, 'account/adminorderdetail.html', context)

def adminHiringOrder(request, pk):
    order = HiringOrder.objects.get(id=pk)
    num = order.id
    form = adminHiringform(instance=order)
    form.fields['employee_order'].choices = list()
    for k in GroupEmployee.objects.all():
        # Append the tuple of OptGroup Name, Organism.
        form.fields['employee_order'].choices.append(
            (

                k.name,  # First tuple part is the optgroup name/label
                list(  # Second tuple part is a list of tuples for each option.
                    (o.id, o.employee_user.first_name) for o in EmployeeProfile.objects.filter(group=k).order_by('employee_user')
                    # Each option itself is a tuple of id and name for the label.
                )
            )
        )

    if request.method == 'POST':
        form = adminHiringform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            #sending notification when assign the job to employee
            em = order.employee_order.employee_user.email
            subject = order.address
            deliverdate = order.leash_date
            send_mail(
                'New Job Request',
                'You have a Hiring Order Required to deliver to ' + str(subject) + 'on' +str(deliverdate) + '\n' +'Please Login in to Your Account to Confirm it',
                'dcf1996028@gmail.com',
                [em],
                fail_silently=False,
            )
            messages.success(request, 'HiringOrder' + str(num) + 'has been assgined')
            return redirect('account:admin_dashboard')

    context = {'form': form}
    return render(request, 'account/adminorderdetail.html', context)


def admindeleteorder(request,pk):

    order = Order.objects.get(id=pk)
    num = order.id
    if request.method == "POST":
        order.delete()
        messages.success(request, 'Order ' + str(num) + ' deleted')
        return redirect('account:assignedOrders')
    context = {'order':order}

    return render(request,'account/admindeleteorderconfirm.html',context)


def admindeletehiringorder(request,pk):

    order = HiringOrder.objects.get(id=pk)
    num = order.id
    if request.method == "POST":
        order.delete()
        messages.success(request, 'Hiringorder ' + str(num) + ' deleted')
        return redirect('account:assignedOrders')
    context = {'order':order}

    return render(request,'account/admindeletehiringorderconfirm.html',context)

def payserviceorder(request, pk):

    ins = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        ins.isPaid = True
        ins.save()
        messages.success(request, 'Order ' + str(ins.id) + ' has been paid')
        return redirect('account:customerOrder')

    return render(request, 'account/paymentPage.html')


def payhiringorder(request, pk):

    ins = get_object_or_404(HiringOrder, pk=pk)
    if request.method == "POST":
        ins.isPaid = True
        ins.save()
        messages.success(request, 'Order ' + str(ins.id) + ' has been paid')
        return redirect('account:customerOrder')

    return render(request, 'account/paymentPage.html')


# admin to manage employee account and profile
def adminManageEmployee(request,pk):
    emp = EmployeeProfile.objects.get(id=pk)
    form = adminManageEmployeeform(instance=emp)
    if request.method == 'POST':
        form = adminManageEmployeeform(request.POST, instance=emp)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'account/adminManageEmployee.html',context)


def employeeJobs(request):

    if request.user.is_staff and not request.user.is_superuser:
        user = request.user.employeeprofile
        order = Order.objects.filter(employee_order=user)
        hiring = HiringOrder.objects.filter(employee_order=user)
        context = {
            'orders': order,
            'hiring': hiring,

        }

        return render(request, 'account/Employee_Jobs.html',context)
    else:
        return HttpResponse("you are not staff")

def employeeDashboard(request):
    if request.user.is_staff and not request.user.is_superuser:
        user = request.user.employeeprofile
        order = Order.objects.filter(employee_order=user)
        hiring = HiringOrder.objects.filter(employee_order=user)
        context = {
            'orders': order,
            'hiring':hiring,

        }

        return render(request, 'account/Employee_Dash.html',context)
    else:
        return HttpResponse("you are not staff")

def employeeTimesheet(request):
    return render(request, 'account/Timesheet.html')



def customerorderfeedback(request, pk):
    if request.method == "POST":
        order = Order.objects.get(id=pk)
        fd = request.POST['comments']
        order.feedbackCTE = fd
        order.save()
        return redirect('account:customerPreOrder')

    # form = orderfeedback(instance=order)
    # if request.method == 'POST':
    #     form = orderfeedback(request.POST, instance=order)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('account:customerPreOrder')
    #
    # context = {'form': form}
    return render(request, 'account/customerorderfeedback.html')


def employeeorderfeedback(request, pk):
    if request.method == "POST":

        order = Order.objects.get(id=pk)
        fd = request.POST['comments']
        order.feedbackETC = fd
        order.save()
        return redirect('account:employeeJobs')
    # form = orderfeedbackETC(instance=order)
    # if request.method == 'POST':
    #     form = orderfeedbackETC(request.POST, instance=order)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/ServiceOrderlist/')
    #
    # context = {'form': form}
    return render(request, 'account/employeeorderfeedback.html')


def employee_order_job_done(request, pk):
    ins = get_object_or_404(Order, pk=pk)
    ins.isDone = True
    ins.save()
    messages.success(request, 'Order ' + str(ins.id) + ' Done')
    return redirect('account:employeeJobs')

def employee_hiringorder_job_done(request, pk):
    ins = get_object_or_404(HiringOrder, pk=pk)
    ins.isDone = True
    ins.save()
    messages.success(request, 'Order ' + str(ins.id) + ' Done')
    return redirect('account:employeeJobs')


def ServiceOrderdetail(request, pk):
    ins = get_object_or_404(Order, pk=pk)
    context = {
        'object': ins
    }
    return render(request, 'account/serviceorderdetail.html', context)


def HiringOrderdetail(request, pk):
    ins = get_object_or_404(HiringOrder, pk=pk)
    context = {
        'object': ins
    }
    return render(request, 'account/Hiringorderdetail.html', context)


def ServiceOrderlist(request):
    if request.user.is_staff and not request.user.is_superuser:
        user = request.user.employeeprofile
        order = Order.objects.filter(employee_order=user)

        context = {
            'orders': order,

        }
        return render(request, 'account/serviceorderlist.html', context)
    else:
        return HttpResponse('You are not staff')


def HiringOrderlist(request):
    user = request.user.employeeprofile
    order = HiringOrder.objects.filter(employee_order=user)
    context = {
        'orders': order
    }
    return render(request, 'account/hiringorderlist.html', context)


def accpet_HiringOrder(request, pk):
    ins = get_object_or_404(HiringOrder, pk=pk)
    # ins.employee_order = request.user.employeeprofile
    ins.assigned = True
    ins.save()
    messages.success(request, 'Order ' + str(ins.id) + ' has been accepted')
    return redirect('account:employee_dashboard')


def accpet_ServiceOrder(request, pk):
    ins = get_object_or_404(Order, pk=pk)
    # ins.employee_order = request.user.employeeprofile
    ins.assigned = True
    ins.save()
    messages.success(request, 'Order ' + str(ins.id) + ' has been accepted')
    return redirect('account:employee_dashboard')


def decline_ServiceOrder(request, pk):
    ins = get_object_or_404(Order, pk=pk)
    ins.employee_order = None
    ins.save()
    messages.success(request, 'You decline the order: '+ str(ins.id))
    return redirect('account:employee_dashboard')





def checkout(request):
    leashdate = request.POST['ld']
    returndate = request.POST['rd']
    service_address = request.POST['address']
    service_geo = request.POST['geolocation']
    test3 = request.POST.get('way', False)

    if test3 == 'pickup':

        customer = request.user.customerprofile
        hiringorder, created = HiringOrder.objects.get_or_create(cus_order=customer, complete=False)
        hiringorder.date_order=datetime.now()
        hiringorder.complete = True
        hiringorder.isPickup = True
        hiringorder.leash_date = leashdate
        hiringorder.return_date = returndate
        hiringorder.save()
        ins = hiringorder.cartitem_set.all()
        for i in ins:
            eq = get_object_or_404(Equipment, pk=i.equipment.id)
            eq.stock = eq.stock - i.quantity
            eq.save()
        messages.success(request, 'Success book pick up order :' + str(hiringorder.id))
        return redirect('account:customerOrder')
    else:

        pass
    if test3 == 'deliver':

        customer = request.user.customerprofile
        hiringorder, created = HiringOrder.objects.get_or_create(cus_order=customer, complete=False)
        hiringorder.date_order = datetime.now()
        hiringorder.complete = True
        hiringorder.isDelivery = True
        hiringorder.leash_date = leashdate
        hiringorder.return_date = returndate
        hiringorder.address = service_address
        hiringorder.geolocation = service_geo
        hiringorder.save()
        ins = hiringorder.cartitem_set.all()
        for i in ins:
            eq = get_object_or_404(Equipment, pk=i.equipment.id)
            eq.stock = eq.stock - i.quantity
            eq.save()
        messages.success(request, 'Success book delivery euqipment order:' + str(hiringorder.id))
        return redirect('account:customerOrder')
    else:
        pass

    return redirect('account:HireEquipement')



@login_required(login_url='account:login')
def cart(request):
    if not request.user.is_staff and not request.user.is_superuser:
        customer = request.user.customerprofile
        order, created = HiringOrder.objects.get_or_create(cus_order=customer, complete=False)
        form = Hiringbook_form()
        equipment = order.cartitem_set.all()
        context = {
            'equipments': equipment,
            'order': order,
            'form':form
        }
        return render(request, 'account/cart.html', context)
    else:
        return HttpResponse("You are not a customer user account")


def CustomerRegiser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'account/userregister.html', context)


def EmployeeRegiser(request):
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:stafflogin')
    else:
        form = EmployeeRegisterForm(initial={'is_staff': True})

    context = {'form': form}
    return render(request, 'account/employeeregister.html', context)


# this is just for user login
def testlogin(request):
    if request.user.is_authenticated:
        return redirect('account:index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not request.user.is_superuser and not request.user.is_staff:
                    cusprofile, created = CustomerProfile.objects.get_or_create(cus_user=user)
                    cusprofile.save()
                    return redirect('account:index')
                else:
                    logout(request)
                    return HttpResponse("please login a user account")
            else:
                messages.info(request,'Your password or username is incorrect')
    context = {}
    return render(request, 'account/Login.html', context)


def logoutpage(request):
    logout(request)
    return redirect('account:index')


def staffLogin(request):
    if request.user.is_authenticated and request.user.is_staff and not request.user.is_superuser:
        return redirect('account:employee_dashboard')
    elif request.user.is_superuser:
        return redirect('account:admin_dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not request.user.is_superuser and request.user.is_staff:
                    # this code below is script code
                    groupname = GroupEmployee.objects.get(pk=1)
                    eploprofile, created = EmployeeProfile.objects.get_or_create(employee_user=user,group=groupname)
                    eploprofile.save()
                    return redirect('account:employee_dashboard')
                elif request.user.is_superuser:
                    return redirect('account:admin_dashboard')
                else:
                    logout(request)
                    return HttpResponse("you are not staff")
    context = {}
    return render(request, 'account/stafflogintest.html', context)

# Hire Equipment page
def Store(request):
    if request.user.is_authenticated and not request.user.is_staff and not request.user.is_superuser:
        products = Equipment.objects.all()
        customer = request.user.customerprofile
        order, created = HiringOrder.objects.get_or_create(cus_order=customer, complete=False)
        equipment = order.cartitem_set.all()
        cartItem = order.get_cart_items

        context = {
            "products": products,
            'equipments': equipment,
            'order': order,
            'cartItem': cartItem
        }
        return render(request, 'account/Hire_Equipments.html', context)
    else:
        products = Equipment.objects.all()
        context = {
            "products": products,

        }
        return render(request, 'account/Hire_Equipments.html', context)


@login_required(login_url='account:login')
def updateItem(request):

    data = json.loads(request.body)
    equipmentID = data['equipmentID']
    action = data['action']

    customer = request.user.customerprofile
    equipment = Equipment.objects.get(id=equipmentID)
    order, created = HiringOrder.objects.get_or_create(cus_order=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(order=order, equipment=equipment)

    if action == 'add':
        if cartItem.quantity >= equipment.stock:
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



def adminmanageleave(request):
    return render(request,'account/adminmanageleave.html')


def pickuporder(request):
    hiringorder = HiringOrder.objects.all()
    context = {
        'hiringorders': hiringorder
    }

    return render(request,'account/pickuporder.html',context)


@login_required(login_url='account:login')
def customerOrder(request):
    if not request.user.is_staff and not request.user.is_superuser:
        customer = request.user.customerprofile
        order = Order.objects.filter(cus_order=customer)
        hiringorder = HiringOrder.objects.filter(cus_order=customer)
        context = {
            'orders': order,
            'hiringorders': hiringorder
        }
        return render(request, 'account/UserDashPage.html', context)
    else:
        return HttpResponse("you are not user account")

def customerPreOrder(request):
    # if not request.user.is_staff and not request.user.is_superuser:
        customer = request.user.customerprofile
        order = Order.objects.filter(cus_order=customer)
        hiringorder = HiringOrder.objects.filter(cus_order=customer)
        context = {
            'orders': order,
            'hiringorders': hiringorder
        }
        return render(request, 'account/UserpreorderPage.html', context)


def decline_HiringOrder(request,pk):
    ins = get_object_or_404(HiringOrder, pk=pk)
    ins.employee_order = None
    ins.save()
    messages.success(request, 'You decline the order: '+ str(ins.id))
    return redirect('account:employee_dashboard')



def customerprofile(request):
    u_form = userprofileform(instance=request.user.customerprofile)
    uinfo_form = userinfoform(instance=request.user)
    if request.method == 'POST':
        u_form = userprofileform(request.POST, instance=request.user.customerprofile)
        uinfo_form = userinfoform(request.POST,instance=request.user)

        if u_form.is_valid() and uinfo_form.is_valid():
            u_form.save()
            uinfo_form.save()
            messages.success(request,"Your info updated")
            return redirect('account:customerprofile')
        else:
            u_form = userprofileform(request.POST, instance=request.user.customerprofile)
            uinfo_form = userinfoform(request.POST, instance=request.user)
    context={
        'uform':u_form,
        'uinfoform':uinfo_form
    }

    return render(request,'account/ManageProfile.html',context)


def staffprofile(request):
    u_form = staffprofileform(instance=request.user.employeeprofile)
    uinfo_form = staffinfoform(instance=request.user)
    if request.method == 'POST':
        u_form = userprofileform(request.POST, instance=request.user.customerprofile)
        uinfo_form = userinfoform(request.POST,instance=request.user)

        if u_form.is_valid() and uinfo_form.is_valid():
            u_form.save()
            uinfo_form.save()
            messages.success(request,"Your info updated")
            return redirect('account:customerprofile')
        else:
            u_form = userprofileform(request.POST, instance=request.user.customerprofile)
            uinfo_form = userinfoform(request.POST, instance=request.user)
    context={
        'uform':u_form,
        'uinfoform':uinfo_form
    }

    return render(request,'account/staffManageProfile.html',context)