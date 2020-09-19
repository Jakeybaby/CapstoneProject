import json
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from Oneshop.models import *
from django_google_maps.widgets import GoogleMapsAddressWidget

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']

class EmployeeRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2','is_staff']

class adminform(ModelForm):

    employee_order = forms.ModelChoiceField(
        queryset=EmployeeProfile.objects.all().order_by('group__name', 'employee_user')
    )
    class Meta:
        model = Order
        fields = ['employee_order','cus_order','address','geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap',
            'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'],
            'componentRestrictions': {'country': 'NZ'}
            })
         }),
        }

class adminManageEmployeeform(ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'

class servicebook_form(ModelForm):
    class Meta:
        model = Order
        fields = ['address','geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap',
                'data-autocomplete-options': json.dumps({'types': ['geocode','establishment'],
                'componentRestrictions': {'country': 'NZ'}
                })
            }),
        }

class orderfeedback(ModelForm):
    class Meta:
        model = Order
        fields = ['feedbackCTE']


class orderfeedbackETC(ModelForm):
    class Meta:
        model = Order
        fields = ['feedbackETC']


