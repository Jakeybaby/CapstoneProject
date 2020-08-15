from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomerProfile, TimeSheet, EmployeeProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(cus_user=instance)


@receiver(post_save, sender=EmployeeProfile)
def create_employee_timesheet(sender, instance, created, **kwargs):
    if created:
        TimeSheet.objects.create()