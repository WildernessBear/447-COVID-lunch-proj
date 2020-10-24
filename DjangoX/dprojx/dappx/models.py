from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class SchoolDistrict(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class School(models.Model):
    district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Menu(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=80)
    # what do these meals actually look like??
    meal_ls = []

    def __str__(self):
        return self.name