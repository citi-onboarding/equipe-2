from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Car(models.Model):
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Model = models.CharField(max_length=30)
    Year = models.CharField(max_length=4)
    Plate = models.CharField(primary_key=True,max_length=7)
    Date = models.DateField(auto_now_add=True)
    Availability = models.BooleanField()
    def __str__(self):
		return self.Model

class User(AbstractUser):
    Nationality = models.CharField(max_length=50)
    Age = models.IntegerField()
    #GENDER = (
    #    ('Male', 'Male'),
    #    ('Female', 'Female'),
    #    ('Other', 'Other'),
    #)
    #Gender = models.CharField(max_length=10, choices=GENDER)