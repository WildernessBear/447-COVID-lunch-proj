from django.http import HttpResponse
from django.shortcuts import render
from .models import SchoolDistrict, School, Menu, Meal


def menu(response, id):
    try:
        school = School.objects.get(pk=id)
        text = school.name
        print(school.name)

        if school.menu_set.exists():
            for menu in school.menu_set.all():
                print(menu.name)
                for item in menu.meal_set.all():
                    print(' - ', item.name, ': ', item.description)
        else:
            print('menu does not exist')
    except:
        text = 'school does not exist'

    return HttpResponse("%s" %text)