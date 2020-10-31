from django.http import HttpResponse
from django.shortcuts import render
from .models import SchoolDistrict, School, Menu, Meal

class MenuObj():
    name = ''
    meal_ls = []
    description_ls = []
    def __str__(self):
        return self.name

def menu_view(response, id):
    try:
        school = School.objects.get(pk=id)

        # this dictionary will be passed to the template
        context = {
            'school': school.name,
            'menu_ls': []
        }

        text = school.name
        print(school.name)

        if school.menu_set.exists():
            # remove print statements later!
            for menu in school.menu_set.all():
                print(menu.name)
                temp_menu = MenuObj()
                temp_menu.name = menu.name
                for item in menu.meal_set.all():
                    temp_menu.meal_ls.append(item.name)
                    temp_menu.description_ls.append(item.description)
                    print(' - ', item.name, ': ', item.description)
                context['menu_ls'].append(temp_menu)
            print(context['menu_ls'][0].meal_ls)
        else:
            print('menu does not exist')
    except:
        text = 'school does not exist'

    #return HttpResponse("%s" %text)
    return render(response, 'menu.html', context)