from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomerProfile(models.Model):
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    phone = models.TextField(max_length=100, blank=True, null=True)
    cus_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname


class EmployeeProfile(models.Model):
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    phone = models.TextField(max_length=20, blank=True, null=True)
    employee_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
