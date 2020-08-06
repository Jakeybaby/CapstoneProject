from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractUser

from django.db import models


class Admin(BaseUserManager):
    def _create_user(self, username, password, email, **kwargs):
        if not username:
            raise ValueError("enter username！")
        if not password:
            raise ValueError("enter password！")
        if not email:
            raise ValueError("enter email！")
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, email, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username, password, email, **kwargs)

    def create_superuser(self, username, password, email, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username, password, email, **kwargs)


class Customer(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    firstName = models.TextField(max_length=20, blank=True)
    lastName = models.TextField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    address = models.TextField(max_length=100, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = Admin()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


class Employee(models.Model):
    firstName = models.TextField(max_length=20, blank=True)
    lastName = models.TextField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    address = models.TextField(max_length=100, blank=True)


    def __str__(self):
        return self.firstName


class Equiement(models.Model):
    stock_number = models.IntegerField(max_length=999, blank=True)
    name = models.CharField(max_length=20, blank=True)
    admin_manage_equ = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=False)
    cus_hire = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return Equiement.name


class Feedback(models.Model):
    description = models.TextField(max_length=255, blank=True)
    employee_feedback = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=False)
    customer_feedback = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return Feedback


class Order(models.Model):
    admin_order = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=False)
    emp_order = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=False)
    cus_order = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return Order
