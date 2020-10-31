from django.http import HttpResponse
from django.shortcuts import render
from .models import SchoolDistrict, School, Menu, Meal

# this holds menu information for a single menu
class MenuObj:
    def __init__(self, name):
        self.name = name
        self.meal_ls = []
    def __str__(self):
        return self.name

# this holds information for a single meal
class MealObj:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def menu_view(response, id):
    try:
        school = School.objects.get(pk=id)

        # this dictionary will be passed to the template
        context = {
            'school': school.name,
            'menu_ls': [],
        }

        text = school.name
        print(school.name)

        if school.menu_set.exists():
            # remove print statements later!
            for menu in school.menu_set.all():
                print(menu.name)
                temp_menu = MenuObj(menu.name)
                #temp_menu.name = menu.name

                for item in menu.meal_set.all():
                    temp_meal = MealObj(item.name, item.description)
                    #temp_meal.name = item.name
                    #temp_meal.description = item.description

                    temp_menu.meal_ls.append(temp_meal)
                    print(temp_meal.name)
                    print(' - ', item.name, ': ', item.description)

                context['menu_ls'].append(temp_menu)
                for i in temp_menu.meal_ls:
                    print(i.name)
        else:
            print('menu does not exist')
    except:
        text = 'school does not exist'

    #return HttpResponse("%s" %text)
    return render(response, 'menu.html', context)