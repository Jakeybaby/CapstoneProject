from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model
from django_google_maps import fields as map_fields
from django.urls import reverse
# Create your models here.

class CustomerProfile(models.Model):
    address = models.TextField(max_length=255,null=True,blank=True)
    phone = models.TextField(max_length=100, blank=True, null=True)
    cus_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cus_user.username

class GroupEmployee(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class EmployeeProfile(models.Model):
    address = models.TextField(max_length=100, blank=True, null=True)
    phone = models.TextField(max_length=20, blank=True, null=True)
    employee_user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupEmployee,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('account:adminManageEmployee',kwargs={"pk":self.id})

    def __str__(self):
        return self.employee_user.username






class TimeSheet(models.Model):
    staff = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True,blank=True)
    Day = models.CharField(max_length=25,null=True,blank=True)
    timeIn = models.DateTimeField(blank=True,null=True)
    timeOut = models.DateTimeField(blank=True,null=True)
    isLast = models.BooleanField(default=False)

    def ti(self):
        return self.timeIn.strftime("%H:%M:%S")

    def to(self):
        return self.timeOut.strftime("%H:%M:%S")

    def hour(self):
        return round((self.timeOut - self.timeIn).seconds/60/60,2)

    def __str__(self):
        return str(self.Day)




