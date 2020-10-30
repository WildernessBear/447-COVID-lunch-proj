from django.http import HttpResponse
from .models import SchoolDistrict, School, Menu, Meal


def menu(response, id):
    try:
        school = School.objects.get(pk=id)
        text = school.name + '\n'
        try:
            (school.menu_set.get(pk=1))
            text += school.menu_set.get(pk=1).name
        except:
            text += 'menu does not exist'
    except:
        text = 'school does not exist'

    return HttpResponse("%s" %text)