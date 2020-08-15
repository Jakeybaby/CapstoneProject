from django.contrib import admin
from .models import *



admin.site.register(Order)
# admin.site.register(EquiementOrder)
admin.site.register(ServicesOrder)
admin.site.register(Equipment)
admin.site.register(Feedback)
admin.site.register(Services)
admin.site.register(CartItem)
admin.site.register(Cart)
