import json
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from Oneshop.models import *
from django_google_maps.widgets import GoogleMapsAddressWidget

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

class EmployeeRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2','is_staff']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'is_staff':None
        }

class applyleaveForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(applyleaveForm, self).__init__(*args, **kwargs)

    class Meta:
        model = leave
        fields = ['StartDate','EndDate','note','staff']

class adminform(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(adminform, self).__init__(*args, **kwargs)
    #     self.fields['geolocation'].hidden = True

    employee_order = forms.ModelChoiceField(
        queryset=EmployeeProfile.objects.all().order_by('group__name', 'employee_user')
    )


    class Meta:
        model = Order
        fields = ['employee_order','address','geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap',
            'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'],
            'componentRestrictions': {'country': 'NZ'}
            })
         }),
        }




class adminHiringform(ModelForm):



    employee_order = forms.ModelChoiceField(
        queryset=EmployeeProfile.objects.all().order_by('group__name', 'employee_user')
    )


    class Meta:
        model = Order
        fields = ['employee_order','address','geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap',
            'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'],
            'componentRestrictions': {'country': 'NZ'}
            })
         }),
        }

    # def __init__(self, *args, **kwargs):
    #     super(adminHiringform, self).__init__(*args, **kwargs)
    #     self.fields['geolocation'].hidden = True



class adminManageEmployeeform(ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['employee_user','group','phone','address']

    def __init__(self, *args, **kwargs):
        super(adminManageEmployeeform, self).__init__(*args, **kwargs)
        self.fields['employee_user'].disabled = True
        self.fields['phone'].disabled = True
        self.fields['address'].disabled = True


class adminManagePropertyservicesform(ModelForm):
    class Meta:
        model = PropetyServices
        fields = ['name','price']


class adminManageSecurityservicesform(ModelForm):
    class Meta:
        model = SecurityServices
        fields = ['name','price']


class adminManageEquipmentform(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['price'].required = True
        self.fields['pic'].required = True
        self.fields['stock'].required = True

    class Meta:
        model = Equipment
        fields = ['name','price','pic','stock']

class servicebook_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = True


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

class Hiringbook_form(ModelForm):
    class Meta:
        model = HiringOrder
        fields = ['address','geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget(attrs={

                'data-map-type': 'roadmap',
                'data-autocomplete-options': json.dumps({'types': ['geocode','establishment'],
                'componentRestrictions': {'country': 'NZ'},

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


class userprofileform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = True
        self.fields['phone'].required = True


    class Meta:
        model = CustomerProfile
        fields = ['address','phone']

class userinfoform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class staffprofileform(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['address','phone']

class staffinfoform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']