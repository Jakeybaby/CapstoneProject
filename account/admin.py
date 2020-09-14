from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
admin.site.register(CustomerProfile)
admin.site.register(EmployeeProfile)
admin.site.register(Rental,RentalAdmin)
# admin.site.register(TimeSheet)

