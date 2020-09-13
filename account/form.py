from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from Oneshop.models import *

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']


class adminform(ModelForm):
    class Meta:
        model = Order
        fields = ['employee_order','cus_order']


class orderfeedback(ModelForm):
    class Meta:
        model = Order
        fields = ['feedbackCTE']


class orderfeedbackETC(ModelForm):
    class Meta:
        model = Order
        fields = ['feedbackETC']