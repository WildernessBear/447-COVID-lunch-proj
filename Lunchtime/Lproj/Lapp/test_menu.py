from django.shortcuts import render
from django.template.loader import render_to_string
from django.test import TestCase, Client
from .models import SchoolDistrict, School, Menu, Meal, MyUser
import django.template.loader

# FOR DATABASE TESTS: classes should be subclasses django.test.TestCase
# ONLY FOR NON-DATABASE TESTS: classes subclasses of unittest.TestCase

# menu models test case
# makes sure the databases associated with models are organized correctly
# breakdown of temp databases:
#   10 districts
#   each district has 10 schools
#   each school has 2 menus
#   each menu has 3 items
#   each item has 3 ingredients
class MenuModelsTestCase(TestCase):
    def setUp(self):
        self.num_districts = 10
        self.num_schools = 10
        self.num_menus = 2
        self.num_items = 3
        self.num_ingredients = 3

        district = 'district'
        school = 'school'
        menu = 'menu'
        item = 'item'
        description = 'description goes here'
        prep = 'prep goes here'
        ingr = 'ingr'

        # create districts
        for i in range(self.num_districts):
            district += str(i)
            temp_district = SchoolDistrict.objects.create(name=district)
            district = 'district'

            # create schools in each district
            for j in range(self.num_schools):
                school += str(j)
                temp_school = temp_district.school_set.create(name=school)
                school = 'school'

                # create menus for each school
                for k in range(self.num_menus):
                    menu += str(k)
                    temp_menu = temp_school.menu_set.create(name=menu)
                    menu = 'menu'

                    # create items for each menu
                    for m in range(self.num_items):
                        item += str(m)
                        temp_meal = temp_menu.meal_set.create(name=item, description=description, prep=prep)
                        item = 'item'

                        # create ingredients for each item
                        for n in range(self.num_ingredients):
                            ingr += str(n)
                            temp_meal.ingredient_set.create(name=ingr)
                            ingr = 'ingr'

    def test_organization_of_db(self):
        print("Running MenuModelsTestCase: test_organization_of_db")

        for district in SchoolDistrict.objects.all():
            for school in district.school_set.all():
                self.assertEqual(district.id, school.district.id)
                for menu in school.menu_set.all():
                    self.assertEqual(school.id, menu.school.id)
                    for meal in menu.meal_set.all():
                        self.assertEqual(menu.id, meal.menu.id)
                        for ingredient in meal.ingredient_set.all():
                            self.assertEqual(meal.id, ingredient.meal.id)

# class MenuTemplatesTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.credentials = {
#             'username': 'george',
#             'password': 'secret',
#             'email': 'email@gmail.com'
#         }
#         self.user = MyUser.objects.create(username = self.credentials['username'], email = self.credentials['email'],password = self.credentials['password'])
#
#     def test_login(self):
#         self.client.login(self.credentials['username'],self.credentials['password'])


# menu template test
# makes sure the correct templates are being used and the correct information is being displayed

# this holds info for a single school
class SchoolObj:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# this holds menu information for a single menu
class MenuObj:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.meal_ls = []

# this holds information for a single meal
class MealObj:
    def __init__(self, id, name, description, prep):
        self.id = id
        self.name = name
        self.description = description
        self.prep = prep
        self.ingredient_ls = []

class MenuTemplatesTestCase(TestCase):
    def setUp(self):
        self.num_districts = 10
        self.num_schools = 10
        self.num_menus = 2
        self.num_items = 3
        self.num_ingredients = 3

        district = 'district'
        school = 'school'
        menu = 'menu'
        item = 'item'
        description = 'description goes here'
        prep = 'prep goes here'
        ingr = 'ingr'

        # create districts
        for i in range(self.num_districts):
            district += str(i)
            temp_district = SchoolDistrict.objects.create(name=district)
            district = 'district'

            # create schools in each district
            for j in range(self.num_schools):
                school += str(j)
                temp_school = temp_district.school_set.create(name=school)
                school = 'school'

                # create menus for each school
                for k in range(self.num_menus):
                    menu += str(k)
                    temp_menu = temp_school.menu_set.create(name=menu)
                    menu = 'menu'

                    # create items for each menu
                    for m in range(self.num_items):
                        item += str(m)
                        temp_meal = temp_menu.meal_set.create(name=item, description=description, prep=prep)
                        item = 'item'

                        # create ingredients for each item
                        for n in range(self.num_ingredients):
                            ingr += str(n)
                            temp_meal.ingredient_set.create(name=ingr)
                            ingr = 'ingr'

    def test_schools_page(self):
        print("Running MenuTemplatesTestCase: test_schools_page")

        sch_context = {
            'school_ls': []
        }

        all_schools = School.objects.all()
        for school in all_schools:
            temp_school = SchoolObj(school.id, school.name)
            sch_context['school_ls'].append(temp_school)

        with self.assertTemplateUsed('Lapp/schools.html'):
            render_to_string('Lapp/schools.html', sch_context)

    def test_meals_page(self):
        print("Running MenuTemplatesTestCase: test_meals_page")

        meal_context = {
            'school': '',
            'menu_ls': [],
            'error': None
        }

        for school in School.objects.all():
            temp_school = SchoolObj(school.id, school.name)
            meal_context['school'] = temp_school

            if school.menu_set.exists():
                for menu in school.menu_set.all():
                    temp_menu = MenuObj(menu.id, menu.name)

                    for item in menu.meal_set.all():
                        temp_meal = MealObj(item.id, item.name, item.description, item.prep)

                        for ingredient in item.ingredient_set.all():
                            temp_meal.ingredient_ls.append(ingredient.name)

                        temp_menu.meal_ls.append(temp_meal)

                    meal_context['menu_ls'].append(temp_menu)

            with self.assertTemplateUsed('Lapp/meals.html'):
                render_to_string('Lapp/meals.html', meal_context)


    def test_meal_page(self):
        print("Running MenuTemplatesTestCase: test_meal_page")

        item_context = {
            'item': '',
            'error': None
        }

        for item in Meal.objects.all():
            temp_meal = MealObj(item.id, item.name, item.description, item.prep)
            for ingredient in item.ingredient_set.all():
                temp_meal.ingredient_ls.append(ingredient.name)
            item_context['item'] = temp_meal
            with self.assertTemplateUsed('Lapp/meal_page.html'):
                render_to_string('Lapp/meal_page.html', item_context)
