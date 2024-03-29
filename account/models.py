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
    address = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    cus_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cus_user.username

class GroupEmployee(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class EmployeeProfile(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    employee_user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupEmployee,on_delete=models.CASCADE,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('account:adminManageEmployee',kwargs={"pk":self.id})

    def viewtimesheet(self):
        return reverse('account:adminviewstafftimesheet', kwargs={"pk": self.employee_user_id})

    def __str__(self):
        return self.employee_user.first_name

    def aa(self):
        try:
            ss = self.timesheet_set.filter(isLast=False)
            total = sum([item.hour() for item in ss])
            return total
        except TypeError:
            pass


class leave(models.Model):
    StartDate = models.DateField(default=datetime.now,null=True,blank=True)
    EndDate = models.DateField(null=True, blank=True)
    staff = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)
    note = models.CharField(max_length=255,null=True,blank=True)
    isApproval = models.BooleanField(default=False)
    isReject = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def approval(self):
        return reverse('account:approval_leave', kwargs={"pk":self.id})

    def reject(self):
        return reverse('account:reject_leave', kwargs={"pk":self.id})


class TimeSheet(models.Model):
    staff = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True,blank=True)
    Day = models.CharField(max_length=25,null=True,blank=True)
    timeIn = models.DateTimeField(blank=True,null=True)
    timeOut = models.DateTimeField(blank=True,null=True)
    isLast = models.BooleanField(default=False)
    isBreak = models.BooleanField(default=False)

    def ti(self):
        return self.timeIn.strftime("%H:%M:%S")

    def to(self):
        return self.timeOut.strftime("%H:%M:%S")

    def hour(self):
        try:
            if self.isBreak == False:
                return round(((self.timeOut - self.timeIn).seconds)/60/60,2)
            elif self.isBreak == True:
                return round(((self.timeOut - self.timeIn).seconds - 1800) / 60 / 60, 2)
        except TypeError:
            return 0

    def __str__(self):
        return str(self.Day)




