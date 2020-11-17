from django.contrib.auth.models import AbstractUser
from django.db import models


# custom user class - currently just exists
class MyUser(AbstractUser):
    pass


class SchoolDistrict(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class School(models.Model):
    objects = None
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

    def __str__(self):
        return self.name
