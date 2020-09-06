from django.db import models
from account.models import *
from django.utils import timezone
from django.urls import reverse


class SecurityServices(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.name


class PropetyServices(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)

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
    date_order = models.DateTimeField(default=timezone.now)

    complete = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    isService = models.BooleanField(default=False)
    isPropety = models.BooleanField(default=False)

    feedbackETC = models.CharField(max_length=255, null=True, blank=True)
    feedbackCTE = models.CharField(max_length=255, null=True, blank=True)

    # @property
    # def get_cart_items(self):
    #     cartitems = self.cartitem_set.all()
    #     total = sum([item.quantity for item in cartitems])
    #     return total
    #
    # @property
    # def get_cart_total(self):
    #     cartitems = self.cartitem_set.all()
    #     total = sum([item.get_total for item in cartitems])
    #     return total


    def checkout(self):
        return reverse('account:checkout')

    def get_absolute_url(self):
        return reverse('account:ServiceOrderdetail',kwargs={"pk":self.id})

    def accpet_job_url(self):
        return reverse('account:accpet_job', kwargs={"pk":self.id})

    def __str__(self):
        return str(self.id)

class HiringOrder(models.Model):
    cus_order = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True, blank=False)
    employee_order = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=False)
    date_order = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
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


    def checkout(self):
        return reverse('account:checkout')

    def get_absolute_url(self):
        return reverse('account:HiringOrderdetail',kwargs={"pk":self.id})

    def accpet_job_url(self):
        return reverse('account:accpet_job', kwargs={"pk":self.id})

    def __str__(self):
        return str(self.id)



class SecurityOrder(models.Model):
    security_service = models.ForeignKey(SecurityServices, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_required = models.DateTimeField(default=datetime.now,blank=True)
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return str(self.security_service.name)


class PropertyOrder(models.Model):
    property_service = models.ForeignKey(PropetyServices, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_required = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.property_service.name


class Feedback(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, blank=True, null=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True, blank=False)

    def __str__(self):
        return str(self.description + ' The rate is:' + str(self.rate))


class ShippingAddress(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


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


