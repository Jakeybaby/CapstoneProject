from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(EquiementOrder)
admin.site.register(ServicesOrder)
admin.site.register(Equiement)
admin.site.register(Feedback)
admin.site.register(Services)