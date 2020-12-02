from django.contrib.auth.models import AbstractUser
from django.db import models


# custom user class - currently just exists
class MyUser(AbstractUser):
    pass


class Student(models.Model):
    school = models.CharField(max_length=100)
    milk = False
    eggs = False
    fish = False
    shellfish = False
    tree_nuts = False
    peanuts = False
    wheat = False
    soybeans = False
    other = models.CharField(max_length=250)


class SchoolDistrict(models.Model):
    objects = None
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


# times for each school
class Time(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# this will hold details of a single meal
class Meal(models.Model):
    objects = None
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=240)
    prep = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name
