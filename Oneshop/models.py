from django.db import models
from account.models import *
from django.utils import timezone


class Services(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.name


class Equiement(models.Model):
    name = models.TextField(max_length=50,null=True,blank=True)
    stock = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    cus_order = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True, blank=False)
    employee_order = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=False)
    date_order = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False, null=True, blank=False)
    service = models.ManyToManyField(Services)
    equiement = models.ManyToManyField(Equiement)
    feedbackETC = models.CharField(max_length=255,null=True,blank=True)
    feedbackCTE = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.cus_order.firstname

# class ServicesOrder(models.Model):
#     service = models.ForeignKey(Services,on_delete=models.SET_NULL,blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
#     data_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.service.name



# class EquiementOrder(models.Model):
#     equiment = models.ForeignKey(Equiement,on_delete=models.SET_NULL,blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
#     qunatity = models.IntegerField(default=0,null=True,blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    description = models.CharField(max_length=255,null=True,blank=True)
    customer = models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL,blank=True,null=True)
    employee = models.ForeignKey(EmployeeProfile,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    rate = models.IntegerField(default=0,null=True,blank=False)



