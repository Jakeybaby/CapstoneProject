from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.

admin.site.register(CustomerProfile)
admin.site.register(EmployeeProfile)

admin.site.register(GroupEmployee)
admin.site.register(TimeSheet)

