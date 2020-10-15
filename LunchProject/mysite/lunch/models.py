from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import authenticate


class CreateUser(models.Model):
    # add: user.has_perm('poll.add_vote')
    # change: user.has_perm('poll.change_vote')
    # delete: user.has_perm('poll.delete_vote')
    # view: user.has_perm('poll.view_vote')

    PARENT = 1  # change, view
    STUDENT = 2  # view
    FACULTY = 3  # add, change, delete, view

    ROLES = (
        (PARENT, 'Parent'),
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)

    # name = models.CharField(max_length=100, null=True)
    # last_name = models.CharField(max_length=100, null=True)
    # roles = models.CharField(max_length=50, choices = ROLES, null=True)
    # date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    role = models.CharField()

    user.profile.role = "parent"
    user.profile.save()
    user.profile.role = "student"
    user.profile.save()
    user.profile.role = "faculty"
    user.profile.save()

    if user.profile.role == "parent":
        # do parent case here
        print("Hello parent")

    elif user.profile.role == "student":
        # do student case here
        print("Hello student")

    elif user.profile.role == "faculty":
        # do faculty case here
        print("Hello faculty")


user = authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
    print("You are authenticated")
else:
    # No backend authenticated the credentials
    print("You shall not pass")
