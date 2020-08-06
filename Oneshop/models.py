from django.db import models
from account.models import *
from django.utils import timezone


class Order(models.Model):

    cus_order = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True, blank=False)
    employee_order = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=False)
    date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(max_length=10,null=True,blank=False)


class Feedback(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    feedback_order_emTocus = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True,blank=False)
    feedback_order_cusToem = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True, blank=False)
    comment = models.CharField(max_length=255, null=True, blank=True)


class Equiement(models.Model):
    name = models.TextField(max_length=50,null=True,blank=True)
    stock = models.IntegerField(max_length=999, null=True, blank=True)
    price = models.IntegerField(max_length=9999, null=True, blank=True)

