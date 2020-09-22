from django.db import models
from account.models import *
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta

class SecurityServices(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.name


class PropetyServices(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    pic = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    cus_order = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True, blank=False)
    employee_order = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=False)
    date_order = models.DateTimeField(default=datetime.now)

    fullName = models.TextField(max_length=50,null=True,blank=True)
    phoneNumber = models.TextField(max_length=20,null=True,blank=True)

    server_date = models.DateTimeField(null=True,blank=True)

    complete = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    isService = models.BooleanField(default=False)
    isPropety = models.BooleanField(default=False)
    isDone = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)

    address = map_fields.AddressField(max_length=200,null=True)
    geolocation = map_fields.GeoLocationField(max_length=100,null=True)

    feedbackETC = models.CharField(max_length=255, null=True, blank=True)
    feedbackCTE = models.CharField(max_length=255, null=True, blank=True)

    def checkout(self):
        return reverse('account:checkout')

    def get_absolute_url(self):
        return reverse('account:ServiceOrderdetail',kwargs={"pk":self.id})

    def admin_get_absolute_url(self):
        return reverse('account:adminOrder',kwargs={"pk":self.id})

    def customer_feedback_url(self):
        return reverse('account:customerorderfeedback',kwargs={"pk":self.id})

    def employee_feedback_url(self):
        return reverse('account:employeeorderfeedback',kwargs={"pk":self.id})

    def accpet_job_url(self):
        return reverse('account:accpet_ServiceOrder', kwargs={"pk":self.id})

    def decline_job_url(self):
        return reverse('account:decline_ServiceOrder', kwargs={"pk":self.id})

    def done_job_url(self):
        return reverse('account:employee_order_job_done', kwargs={"pk":self.id})

    def payserviceorder(self):
        return reverse('account:payserviceorder', kwargs={"pk":self.id})

    @property
    def latepayment(self):
        if (datetime.now().replace(tzinfo=None) - self.date_order.replace(tzinfo=None)) > timedelta(hours=24):
            return True
        else:
            return False


    def __str__(self):
        return str(self.id)


class HiringOrder(models.Model):
    cus_order = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True, blank=False)
    employee_order = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=False)
    date_order = models.DateTimeField(default=datetime.now)

    complete = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)

    isPickup = models.BooleanField(default=False)
    isDelivery = models.BooleanField(default=False)

    address = map_fields.AddressField(max_length=200, null=True,blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True,blank=True)

    fullName = models.TextField(max_length=50, null=True, blank=True)
    phoneNumber = models.TextField(max_length=20, null=True, blank=True)

    leash_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    feedbackETC = models.CharField(max_length=255, null=True, blank=True)
    feedbackCTE = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    @property
    def get_cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def latepayment(self):
        if (datetime.now().replace(tzinfo=None) - self.date_order.replace(tzinfo=None)) > timedelta(hours=24):
            return True
        else:
            return False


    def admin_get_absolute_url(self):
        return reverse('account:adminHiringOrder',kwargs={"pk":self.id})


    def payHiringorder(self):
        return reverse('account:payhiringorder', kwargs={"pk":self.id})

    def checkout(self):
        return reverse('account:checkout')

    def get_absolute_url(self):
        return reverse('account:HiringOrderdetail',kwargs={"pk":self.id})

    def accpet_job_url(self):
        return reverse('account:accpet_HiringOrder', kwargs={"pk":self.id})

    def __str__(self):
        return str(self.id)



class SecurityOrder(models.Model):
    security_service = models.ForeignKey(SecurityServices, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_required = models.DateTimeField(default=datetime.now,blank=True)
    notes = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return str(self.id)


class PropertyOrder(models.Model):
    property_service = models.ForeignKey(PropetyServices, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_required = models.DateTimeField(default=datetime.now, blank=True)
    notes = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

#
# class Feedback(models.Model):
#     description = models.CharField(max_length=255, null=True, blank=True)
#     customer = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, blank=True, null=True)
#     employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
#     rate = models.IntegerField(default=0, null=True, blank=False)
#
#     def __str__(self):
#         return str(self.description + ' The rate is:' + str(self.rate))




class CartItem(models.Model):
    order = models.ForeignKey('HiringOrder', null=True, blank=True, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    @property
    def get_total(self):
        total = self.equipment.price * self.quantity
        return total

    def __str__(self):
        return self.equipment.name


