from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model
from django_google_maps import fields as map_fields
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


    # timesheet = models.OneToOneField('TimeSheet',on_delete=models.CASCADE)


    def __str__(self):
        return self.employee_user.username




# class TimeSheet(models.Model):
#     timeIn = models.DateTimeField(default=datetime.now, blank=True)
#     timeOut = models.DateTimeField(default=datetime.now, blank=True)
#
#     def ti(self):
#         return self.timeIn.strftime("%Y-%m-%d %H:%M:%S")
#
#     def to(self):
#         return self.timeOut.strftime("%Y-%m-%d %H:%M:%S")
#
#     def hour(self):
#         return self.timeOut - self.timeIn



