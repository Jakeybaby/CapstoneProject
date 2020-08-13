from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class CustomerProfile(models.Model):
    address = models.TextField(max_length=255,null=True,blank=True)
    phone = models.TextField(max_length=100, blank=True, null=True)
    cus_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cus_user.username


class EmployeeProfile(models.Model):
    address = models.TextField(max_length=100, blank=True, null=True)
    phone = models.TextField(max_length=20, blank=True, null=True)
    employee_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_user.username
