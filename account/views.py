
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from Oneshop.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .form import *
from django.contrib.auth import login, authenticate, logout
from datetime import datetime,date
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
import json

import stripe

stripe.api_key = "sk_test_51BURg0Bf2WXWLp3KNXQUXA19LuYZZO2GHw3JYmL96QDhgCgwBUfPcMgxqTtTNTFaMG0OkC2E6mbp2KGVTCnBRCWK0063yoA0WI"



def index(request):
    ins = Order.objects.all()
    context={
        'object':ins
    }
    return render(request, 'account/Index.html',context)


def about(request):
    return render(request, 'account/AboutUs.html')



def contact(request):
    return render(request, 'account/Contact.html')


def timesheettest(request):
    user = request.user.employeeprofile
    ins = request.user.employeeprofile.timesheet_set.all()

    test1,created = TimeSheet.objects.get_or_create(Day='Monday', staff=user, isLast=False)
    test2,created = TimeSheet.objects.get_or_create(Day='Tuesday', staff=user, isLast=False)
    test3,created = TimeSheet.objects.get_or_create(Day='Wensday', staff=user, isLast=False)
    test4,created = TimeSheet.objects.get_or_create(Day='Thursday', staff=user, isLast=False)
    test5,created = TimeSheet.objects.get_or_create(Day='Friday', staff=user, isLast=False)
    test6, created = TimeSheet.objects.get_or_create(Day='Saturday', staff=user, isLast=False)
    test7, created = TimeSheet.objects.get_or_create(Day='Sunday', staff=user, isLast=False)

    test1.save()
    test2.save()
    test3.save()
    test4.save()
    test5.save()
    test6.save()
    test7.save()

    context={
        'txt':ins,
        'test':user

    }
    return render(request,'account/Timesheet.html',context)

def reset(request):
    user = request.user.employeeprofile
    firstname = request.user.first_name
    fe = user.aa()
    em = request.user.employeeprofile.employee_user.email
    send_mail(
        'Works hours of total this week',
        'Kia ora, Admin\n\n'+str(firstname)+" work hour of this week is " + str(fe)+ " Hours\n\nKaipara Security Ltd",
        'dengc05@myunitec.ac.nz',
        [em],
        fail_silently=False,
    )
    print(fe)
    ins = request.user.employeeprofile.timesheet_set.all().order_by('-id')
    test1 = TimeSheet.objects.get(Day='Monday', staff=user,isLast=False)
    test2 = TimeSheet.objects.get(Day='Tuesday', staff=user,isLast=False)
    test3 = TimeSheet.objects.get(Day='Wensday', staff=user,isLast=False)
    test4 = TimeSheet.objects.get(Day='Thursday', staff=user,isLast=False)
    test5 = TimeSheet.objects.get(Day='Friday', staff=user,isLast=False)
    test6 = TimeSheet.objects.get(Day='Saturday', staff=user, isLast=False)
    test7 = TimeSheet.objects.get(Day='Sunday', staff=user, isLast=False)
    test1.isLast = True
    test2.isLast = True
    test3.isLast = True
    test4.isLast = True
    test5.isLast = True
    test6.isLast = True
    test7.isLast = True
    test1.save()
    test2.save()
    test3.save()
    test4.save()
    test5.save()
    test6.save()
    test7.save()
    context = {
        'txt': ins,
        # 'total':total
    }
    return redirect('account:employeeTimesheet')
def recordbreak(request):
    userid = request.user.employeeprofile
    if datetime.today().isoweekday() == 1:
        today = TimeSheet.objects.get(staff=userid,Day="Monday",isLast=False)
        today.isBreak = True
        today.save()

    elif datetime.today().isoweekday() == 2:
        today = TimeSheet.objects.get(staff=userid, Day="Tuesday", isLast=False)
        today.isBreak = True
        today.save()
    elif datetime.today().isoweekday() == 3:
        today = TimeSheet.objects.get(staff=userid, Day="Wensday", isLast=False)
        today.isBreak = True
        today.save()
    elif datetime.today().isoweekday() == 4:
        today = TimeSheet.objects.get(staff=userid, Day="Thursday", isLast=False)
        today.isBreak = True
        today.save()
    elif datetime.today().isoweekday() == 5:
        today = TimeSheet.objects.get(staff=userid, Day="Friday", isLast=False)
        today.isBreak = True
        today.save()
    elif datetime.today().isoweekday() == 6:
        today = TimeSheet.objects.get(staff=userid, Day="Saturday", isLast=False)
        today.isBreak = True
        today.save()
    elif datetime.today().isoweekday() == 7:
        today = TimeSheet.objects.get(staff=userid, Day="Sunday", isLast=False)
        today.isBreak = True
        today.save()

    return redirect('account:employeeTimesheet')
def timein(request):
    userid = request.user.employeeprofile
    if datetime.today().isoweekday() == 1:
        today = TimeSheet.objects.get(staff=userid,Day="Monday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()

    elif datetime.today().isoweekday() == 2:
        today = TimeSheet.objects.get(staff=userid,Day="Tuesday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()
    elif datetime.today().isoweekday() == 3:
        today = TimeSheet.objects.get(staff=userid,Day="Wensday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()
    elif datetime.today().isoweekday() == 4:
        today = TimeSheet.objects.get(staff=userid,Day="Thursday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")

        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8,minute=00,second=00):
                today.timeIn = datetime.now().replace(hour=8,minute=00,second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8,minute=00,second=00):
                today.timeIn = datetime.now()
                today.save()

    elif datetime.today().isoweekday() == 5:
        today = TimeSheet.objects.get(staff=userid,Day="Friday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()
    elif datetime.today().isoweekday() == 6:

        today = TimeSheet.objects.get(staff=userid,Day="Saturday",isLast=False)
        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()
    elif datetime.today().isoweekday() == 7:
        today = TimeSheet.objects.get(staff=userid,Day="Sunday",isLast=False)

        try:
            if datetime.now().replace(tzinfo=None) - today.timeIn < timedelta(hours=23):
                messages.success(request, "You already check in")
            else:
                today.timeIn = datetime.now()
                today.save()
        except TypeError:
            if datetime.now() <= datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now().replace(hour=8, minute=00, second=00)
                today.save()
            elif datetime.now() > datetime.now().replace(hour=8, minute=00, second=00):
                today.timeIn = datetime.now()
                today.save()
    return redirect('account:employeeTimesheet')

def timeout(request):
    userid = request.user.employeeprofile
    if datetime.today().isoweekday() == 1:
        today = TimeSheet.objects.get(staff=userid, Day="Monday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request, "You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request, "You haven't check in")
    elif datetime.today().isoweekday() == 2:
        today = TimeSheet.objects.get(staff=userid, Day="Tuesday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request,"You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request,"You haven't check in")
    elif datetime.today().isoweekday() == 3:
        today = TimeSheet.objects.get(staff=userid, Day="Wensday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request, "You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request, "You haven't check in")
    elif datetime.today().isoweekday() == 4:
        today = TimeSheet.objects.get(staff=userid, Day="Thursday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request, "You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request, "You haven't check in")
    elif datetime.today().isoweekday() == 5:
        today = TimeSheet.objects.get(staff=userid, Day="Friday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request, "You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request, "You haven't check in")
    elif datetime.today().isoweekday() == 6:
        today = TimeSheet.objects.get(staff=userid,Day="Saturday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request,"You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request,"You haven't check in")
    elif datetime.today().isoweekday() == 7:
        today = TimeSheet.objects.get(staff=userid,Day="Sunday",isLast=False)
        if today.timeIn:
            try:
                if datetime.now().replace(tzinfo=None) - today.timeOut < timedelta(hours=23):
                    messages.success(request, "You already check out")
                else:
                    today.timeOut = datetime.now()
                    today.save()
            except TypeError:
                today.timeOut = datetime.now()
                today.save()
        else:
            messages.success(request, "You haven't check in")
    return redirect('account:employeeTimesheet')

# def total(request):
#     user = request.user.employeeprofile.employee_user.id
#     test1 = TimeSheet.objects.get(Day='Monday', staff__employee_user_id=user)
#     test2 = TimeSheet.objects.get(Day='Tuesday', staff__employee_user_id=user)
#     test3 = TimeSheet.objects.get(Day='Wensday', staff__employee_user_id=user)
#     test4 = TimeSheet.objects.get(Day='Thursday', staff__employee_user_id=user)
#     test5 = TimeSheet.objects.get(Day='Friday', staff__employee_user_id=user)
#     total = round(test3.hour()+test1.hour()+test2.hour()+test4.hour()+test5.hour(),2)
#     # context={
#     #     'total':total
#     # }
#     return render(request,'account/Timesheet.html')
# --


def admintimesheet(request):
    memeber_list = EmployeeProfile.objects.all().order_by('-id')
    paginator = Paginator(memeber_list, 6)

    page = request.GET.get('page')

    try:
        memeber = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        memeber = paginator.page(1)

    except EmptyPage:
        # If page is out of range deliver last page of results
        memeber = paginator.page(paginator.num_pages)

    context = {'member': memeber}
    return render(request,'account/admintimesheet.html',context)


def adminviewstafftimesheet(request,pk):
    ins = EmployeeProfile.objects.filter(employee_user=pk)
    context= {
        'object': ins
    }
    return render(request,'account/adminviewstafftimesheet.html',context)


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
    messages.success(request,'Your new job'+ str(order.id) +'request has been created')
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
    messages.success(request,'Your new job'+ str(order.id) +'request has been created')
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



def portal(request):
    return render(request, 'account/LearningPortal.html')


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
    if request.user.is_superuser:
        order = Order.objects.all()
        hiringorder_list = HiringOrder.objects.all().filter(isDelivery=True, employee_order=None).order_by('-id')
        paginator = Paginator(hiringorder_list, 2)

        page = request.GET.get('page')

        try:
            hiringorder = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            hiringorder = paginator.page(1)

        except EmptyPage:
            # If page is out of range deliver last page of results
            hiringorder = paginator.page(paginator.num_pages)

        context = {
            'object': order,
            'hiringorders':hiringorder
        }
        return render(request, 'account/Admin_D.html', context)
    else:
        return HttpResponse("You are not admin")



def adminemployeepage(request):
    memeber = EmployeeProfile.objects.all()
    context = {'member':memeber}
    return render(request,'account/adminemployeepage.html',context)


# to see the detail of each order
def adminOrder(request, pk):
    order = Order.objects.get(id=pk)
    num = order.id
    form = adminform(instance=order)
    form.fields['geolocation'].widget = forms.HiddenInput()
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
            name = order.employee_order.employee_user.first_name
            subject = order.address
            jobdate = order.server_date
            send_mail(
                'New Job Request',
                'Kia ora, '+name+'\n\nYou have a New Order Request to \n' + str(subject)+"\n" + 'On ' + str(jobdate) + '\n' +'Please Login in to Your Account to Confirm it\n\nKaipara security Limited',
                'dengc05@myunitec.ac.nz',
                [em],
                fail_silently=False,
            )
            messages.success(request, 'Job request id ' +str(num)+' has been assigned and waiting for the reply from the employee')
            return redirect('account:admin_dashboard')

    context = {'form': form}
    return render(request, 'account/adminorderdetail.html', context)

def adminHiringOrder(request, pk):
    order = HiringOrder.objects.get(id=pk)
    num = order.id
    form = adminHiringform(instance=order)
    form.fields['geolocation'].widget = forms.HiddenInput()
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
            name = order.employee_order.employee_user.first_name
            subject = order.address
            deliverdate = order.leash_date
            send_mail(
                'New Job Request',
                'Kia ora, '+name+'\n\nYou have a Hiring Order Required to deliver to ' + str(subject)+"\n"+ 'On ' +str(deliverdate) + '\n' +'Please Login in to Your Account to Confirm it\n\nKaipara security Limited',
                'dengc05@myunitec.ac.nz',
                [em],
                fail_silently=False,
            )
            messages.success(request, 'Job request id ' +str(num)+' has been assigned and waiting for the reply from the employee')
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


def userdeleteorder(request,pk):

    order = Order.objects.get(id=pk)
    num = order.id
    if request.method == "POST":
        order.delete()
        messages.success(request, 'Order ' + str(num) + ' deleted')
        return redirect('account:customerOrder')
    context = {'order':order}

    return render(request,'account/userdeleteorderconfirm.html',context)


def userdeletehiringorder(request,pk):

    order = HiringOrder.objects.get(id=pk)
    num = order.id
    if request.method == "POST":
        order.delete()
        messages.success(request, 'Hiringorder ' + str(num) + ' deleted')
        return redirect('account:customerOrder')
    context = {'order':order}

    return render(request,'account/userdeletehiringorderconfirm.html',context)

def payserviceorder(request, pk):


    ins = get_object_or_404(Order, pk=pk)
    aa = ins.propertyorder_set.all()
    user = request.user
    em = user.email
    for i in aa:
        ss = int(i.property_service.price)
        dd = i.property_service.name
    if request.method == "POST":
        ins.isPaid = True
        ins.save()
        messages.success(request, 'Order ' + str(ins.id) + ' has been paid')

        customer = stripe.Customer.create(
            email=user.email,
            name=user.first_name,

        )
        charge = stripe.Charge.create(

            amount = ss*100,
            currency = 'nzd',
            source='tok_visa',
            description = 'test',
        )

        send_mail(
            'Customer Order '+ str(ins.id) + " Invoice",
            'Hi '+ user.first_name+ ',\nYour order has successful pay to kairpara Limited LTD\n'
                                    'The total amount of charge is '+str(ss)+'\n'
                                                                             'Order item:\n'
                                                                             'Name             Price\n'
                                                                             +str(dd)+'                    '+str(ss),
            'dengc05@myunitec.ac.nz',
            [em],
            fail_silently=False,
        )
        return redirect('account:customerOrder')

    context={
        'ins':ins,
        'user':user,
        'ss':ss

    }
    return render(request, 'account/paymentPage.html',context)


def payserviceorderse(request, pk):


    ins = get_object_or_404(Order, pk=pk)
    aa = ins.securityorder_set.all()
    user = request.user
    em = user.email
    for i in aa:
        ss = int(i.security_service.price)
        dd = i.security_service.name
    if request.method == "POST":
        ins.isPaid = True
        ins.save()
        messages.success(request, 'Order ' + str(ins.id) + ' has been paid')

        customer = stripe.Customer.create(
            email=user.email,
            name=user.first_name,

        )
        charge = stripe.Charge.create(

            amount = ss*100,
            currency = 'nzd',
            source='tok_visa',
            description = 'test',
        )

        send_mail(
            'Customer Order '+ str(ins.id) + " Invoice",
            'Hi '+ user.first_name+ ',\nYour order has successful pay to kairpara Limited LTD\n'
                                    'The total amount of charge is '+str(ss)+'\n'
                                                                             'Order item:\n'
                                                                             'Name             Price\n'
                                                                             +str(dd)+'                    '+str(ss),
            'dengc05@myunitec.ac.nz',
            [em],
            fail_silently=False,
        )
        return redirect('account:customerOrder')

    context={
        'ins':ins,
        'user':user,
        'ss':ss

    }
    return render(request, 'account/paymentPagese.html',context)


def payhiringorder(request, pk):

    ins = get_object_or_404(HiringOrder, pk=pk)
    aa = ins.cartitem_set.all()
    for i in aa:
        eq = i.equipment.name
        eqprice = i.equipment.price

    user = request.user
    ss = int(ins.get_cart_total)
    em = user.email

    if request.method == "POST":
        ins.isPaid = True
        ins.save()
        messages.success(request, 'Order ' + str(ins.id) + ' has been paid')
        customer = stripe.Customer.create(
            email=user.email,
            name=user.first_name,

        )
        charge = stripe.Charge.create(

            amount=ss * 100,
            currency='nzd',
            source='tok_visa',
            description='test',
        )

        send_mail(
            'Customer Order ' + str(ins.id) + " Invoice",
            'Hi ' + user.first_name + ',\nYour order has successful pay to kairpara Limited LTD\n'
                                      'The total amount of charge is $' + str(ss) + '\n'
                                                                                   'Order item:\n'
                                                                                   'Name             Price\n'
                                                                                    + str(eq) + '                  ' + str(eqprice),
            'dengc05@myunitec.ac.nz',
            [em],
            fail_silently=False,
        )
        return redirect('account:customerOrder')
    context = {
        'ins': ins,
        'user': user,
        'ss': ss

    }
    return render(request, 'account/hiringpaymentPage.html',context)


# admin to manage employee account and profile
def adminManageEmployee(request,pk):
    emp = EmployeeProfile.objects.get(id=pk)
    form = adminManageEmployeeform(instance=emp)
    if request.method == 'POST':
        form = adminManageEmployeeform(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('account:adminemployeepage')

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


def approval_leave(request, pk):
    ins = get_object_or_404(leave, pk=pk)
    ins.isApproval = True
    ins.save()

    return redirect('account:adminmanageleave')

def reject_leave(request, pk):
    ins = get_object_or_404(leave, pk=pk)
    ins.isReject = True
    ins.save()

    return redirect('account:adminmanageleave')


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
            username=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
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
            username = form.cleaned_data.get('username')
            messages.success(request, 'New employee account has been created for' + username)
            return redirect('account:adminemployeepage')
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
                    # groupname = GroupEmployee.objects.get(pk=1)
                    eploprofile, created = EmployeeProfile.objects.get_or_create(employee_user=user)
                    tt = request.user.employeeprofile
                    ts1, created = TimeSheet.objects.get_or_create(staff=tt, Day="Monday",isLast=False)
                    ts2, created = TimeSheet.objects.get_or_create(staff=tt, Day="Tuesday",isLast=False)
                    ts3, created = TimeSheet.objects.get_or_create(staff=tt, Day="Wensday",isLast=False)
                    ts4, created = TimeSheet.objects.get_or_create(staff=tt, Day="Thursday",isLast=False)
                    ts5, created = TimeSheet.objects.get_or_create(staff=tt, Day="Friday",isLast=False)
                    ts6, created = TimeSheet.objects.get_or_create(staff=tt, Day="Saturday", isLast=False)
                    ts7, created = TimeSheet.objects.get_or_create(staff=tt, Day="Sunday", isLast=False)
                    eploprofile.save()
                    ts1.save()
                    ts2.save()
                    ts3.save()
                    ts4.save()
                    ts5.save()
                    ts6.save()
                    ts7.save()

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
    ins_list = leave.objects.all().order_by('-id')
    paginator = Paginator(ins_list, 7)
    page = request.GET.get('page')
    try:
        ins = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        ins = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        ins = paginator.page(paginator.num_pages)
    context={
        'object':ins
    }
    return render(request,'account/adminmanageleave.html',context)


def pickuporder(request):
    hiringorder_list = HiringOrder.objects.filter(isPickup=True).order_by('-id')
    paginator = Paginator(hiringorder_list, 10)
    page = request.GET.get('page')
    try:
        hiringorder = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        hiringorder = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        hiringorder = paginator.page(paginator.num_pages)
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
            messages.success(request,"Your profile has been updated successfully")
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
        u_form = staffprofileform(request.POST, instance=request.user.employeeprofile)
        uinfo_form = staffinfoform(request.POST,instance=request.user)

        if u_form.is_valid() and uinfo_form.is_valid():
            u_form.save()
            uinfo_form.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect('account:staffprofile')
        else:
            u_form = staffprofileform(request.POST, instance=request.user.employeeprofile)
            uinfo_form = staffinfoform(request.POST, instance=request.user)
    context={
        'uform':u_form,
        'uinfoform':uinfo_form
    }

    return render(request,'account/staffManageProfile.html',context)

def applyleave(request):
    us = request.user.employeeprofile
    startdate = request.POST['a']
    enddate = request.POST['b']
    s = request.POST['c']
    leaveapply = leave.objects.create(staff=us,StartDate=startdate,EndDate=enddate,note=s)

    return redirect('account:applyleavePage')


def applyleavePage(request):
    ins_list = leave.objects.filter(staff=request.user.employeeprofile).order_by('-id')
    paginator = Paginator(ins_list, 3)
    page = request.GET.get('page')
    try:
        ins = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        ins = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        ins = paginator.page(paginator.num_pages)
    context={
        'object':ins
    }

    return render(request,'account/staffapplyleave.html',context)


def manageServices(request):
    SSall = SecurityServices.objects.all()
    PSall = PropetyServices.objects.all()
    eqm = Equipment.objects.all()
    context={
        "ssall":SSall,
        'psall':PSall,
        'eq':eqm
    }
    return render(request,'account/manageService.html',context)


def manageequipments(request):

    eqm = Equipment.objects.all()
    context={

        'eq':eqm
    }
    return render(request,'account/manageequipment.html',context)


def changeServices(request,pk):
    ins = PropetyServices.objects.get(id=pk)
    form = adminManagePropertyservicesform(instance=ins)
    if request.method == "POST":
        form = adminManagePropertyservicesform(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            messages.success(request, "ok done")
            return redirect('account:manageServices')
    context = {'form':form}

    return render(request,'account/changeservice.html',context)


def deletePropertyServices(request,pk):
    ins = PropetyServices.objects.get(id=pk)
    if request.method == "POST":

        ins.delete()
        return redirect('account:manageServices')
    context={'order':ins}
    return render(request,'account/admindeletePS.html',context)

def changeSecurityServices(request,pk):
    ins = SecurityServices.objects.get(id=pk)
    form = adminManageSecurityservicesform(instance=ins)
    if request.method == "POST":
        form = adminManageSecurityservicesform(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            messages.success(request, "ok done")
            return redirect('account:manageServices')
    context = {'form':form}

    return render(request,'account/changeSecurityservice.html',context)


def deleteSecurityServices(request,pk):
    ins = SecurityServices.objects.get(id=pk)
    if request.method == "POST":
        ins.delete()

        return redirect('account:manageServices')
    context ={
        'order':ins
    }
    return render(request,'account/admindeleteSS.html',context)


def changeEquipment(request,pk):
    ins = Equipment.objects.get(id=pk)
    form = adminManageEquipmentform(instance=ins)
    if request.method == "POST":
        form = adminManageEquipmentform(request.POST,request.FILES, instance=ins)
        print('sdf')
        if form.is_valid():
            form.save()
            messages.success(request, "ok done")
            return redirect('account:manageequipments')
    context = {'form':form}

    return render(request,'account/changeequipment.html',context)


def deleteequipment(request,pk):
    ins = Equipment.objects.get(id=pk)
    if request.method == "POST":
        ins.delete()
        return redirect('account:manageequipments')
    context ={'order':ins}
    return render(request,'account/admindeleteEQ.html',context)



def addSS(request):
    if request.method =="POST":
        form = adminManageSecurityservicesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:manageServices')
    else:
        form = adminManageSecurityservicesform()

    context = {'form': form}
    return render(request,'account/addSS.html',context)

def addPS(request):
    if request.method == "POST":
        form = adminManagePropertyservicesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:manageServices')
    else:
        form = adminManagePropertyservicesform()

    context = {'form': form}
    return render(request, 'account/addSS.html', context)


def addEQ(request):
    if request.method == "POST":
        form = adminManageEquipmentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account:manageequipments')
    else:
        form = adminManageEquipmentform()

    context = {'form': form}
    return render(request, 'account/addEQ.html', context)




