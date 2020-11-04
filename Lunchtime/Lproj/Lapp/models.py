from django.db import models
from django.contrib.auth.models import AbstractUser


# custom user class - currently just exists
class MyUser(AbstractUser):
    pass


class SchoolDistrict(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class School(models.Model):
    district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# menu for maybe the day of the week??
class Menu(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# this will hold details of a single meal
class Meal(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=240)
    preparations = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# holds info about projected number of meals per day, per location
class TotalMeals(models.Model):
    location_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    date = models.DateField()
    num_meals = models.IntegerField()

    def __str__(self):
        return self.location_name
