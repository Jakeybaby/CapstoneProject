from django.contrib import admin
from .models import *



admin.site.register(Order)
admin.site.register(SecurityOrder)
admin.site.register(PropertyOrder)
admin.site.register(Equipment)
admin.site.register(Feedback)
admin.site.register(PropetyServices)
admin.site.register(SecurityServices)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)

