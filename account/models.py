from django.db import models

# Create your models here.

class Customer_profile(models.Model):

	firstname = models.CharField(max_length=30, blank = True, null= True)
	lastname = models.CharField(max_length=30, blank = True, null= True)
	address = models.TextField(max_length=100, blank = True, null= True)
	phone = models.Integerfield(max_length=20, blank= True, null = True)
	user = 
	def __str__(self):

		

class Employee_profile(models.Model):

	firstname = models.CharField(max_length=30, blank = True, null=True)
	lastname = models.CharField(max_length=30, blank = True, null=True)
		