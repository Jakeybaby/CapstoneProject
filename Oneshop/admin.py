from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json
class OrderGeo(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap',
            'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'],
            'componentRestrictions': {'country': 'NZ'}
            })
         })},
    }


class HiringGeo(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap',
            'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'],
            'componentRestrictions': {'country': 'NZ'}
            })
         })},
    }



admin.site.register(HiringOrder,HiringGeo)
admin.site.register(Order,OrderGeo)
admin.site.register(SecurityOrder)
admin.site.register(PropertyOrder)
admin.site.register(Equipment)
admin.site.register(PropetyServices)
admin.site.register(SecurityServices)
admin.site.register(CartItem)


