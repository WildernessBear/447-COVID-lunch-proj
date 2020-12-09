from django.contrib.auth import authenticate  # , login, logout
from django.template.loader import render_to_string
from django.test import TestCase, Client
from .models import SchoolDistrict, School, Meal, MyUser  # , Menu
import random

# FOR DATABASE TESTS: classes should be subclasses django.test.TestCase
# ONLY FOR NON-DATABASE TESTS: classes subclasses of unittest.TestCase or django.test.SimpleTestCase

# menu models test case
# makes sure the databases associated with models are organized correctly
# breakdown of temp databases:
#   10 districts
#   each district has 10 schools
#   each school has 2 menus
#   each menu has 3 items
#   each item has 3 ingredients


# description should NOT be seen on website, it just describes if an item is a main dish, side, or drink
class Item:
    def __init__(self, name, description, prep, ingredient_ls):
        self.name = name
        self.description = description
        self.prep = prep
        self.ingredient_ls = ingredient_ls


def set_up_db(apps, schema_editor):
    main = "main"
    side = "side"
    drink = "drink"
    prep1 = "No preparation required"

    breakfast = "Breakfast"
    lunch = "Lunch"

    # just one school district
    district = "Baltimore County"

    schools = ["Arbutus Elementary", "Arbutus Middle", "Catonsville High", "Catonsville Middle", "Chesapeake High",
               "Cockeysville Middle", "Deep Creek Middle", "Deer Park Middle", "Dulaney High", "Dumbarton Middle",
               "Dundalk High", "Dundalk Middle", "Eastern Tech High", "Franklin High", "Franklin Middle",
               "Golden Ring Middle", "Hereford High", "Hereford Middle", "Holabird Middle", "Kenwood High",
               "Lansdowne High", "Lansdowne Middle", "Loch Raven High", "Middle River Middle", "Overlea High",
               "Owings Mills High", "Parkville High", "Parkville Middle", "Perry Hall High", "Perry Hall Middle",
               "Pikesville High", "Pikesville Middle", "Pine Grove Middle", "Randallstown High", "Ridgely Middle",
               "Stemmers Run Middle", "Towson High School", "Windsor Mill Middle", "Woodlawn High", "Woodlawn Middle"]

    # two types of menu, breakfast and lunch
    menu = ["Breakfast", "Lunch"]

    lunch_main_ls = [
        Item("Cheese Pizza", main, None,
             ["whole grain crust", "tomato sauce", "mozzarella cheese"]),
        Item("Pepperoni Pizza", main, None,
             ["whole grain crust", "tomato sauce", "mozzarella cheese", "pepperoni"]),
        Item("Chicken Patty Sandwich", main, None,
             ["chicken breast patty", "hamburger bun", "lettuce", "tomato"]),
        Item("PB & J Sandwich", main, None,
             ["peanut butter", "grape jelly", "whole grain bread"])
    ]

    lunch_side_ls = [
        Item("Choice of Seasonal Fruit", side, None,
             ["apple", "banana", "pear", "orange"]),
        Item("Yogurt Cup", side, None,
             ["Trix yogurt"]),
        Item("Choice of Chip Snack", side, None,
             ["Cheez-it Crackers", "Doritos Nacho Cheese", "Utz Classic Potato Chips",
              "Utz Salt and Vinegar Chips", "Famous Amos Chocolate Chip Cookies"]),
        Item("Vegetable Sticks with Ranch Dressing", side, None,
             ["celery", "carrots", "broccoli", "ranch dressing"])
    ]

    breakfast_main_ls = [
        Item("Assorted Cold Cereal", main, "Requires milk",
             ["Cinnamon Chex", "Frosted Mini Wheats", "Honey Nut Cheerios", "Raisin Bran"]),
        Item("Bagel and Cream Cheese", main, None,
             ["whole wheat bagel", "cream cheese"]),
        Item("Mini Cinnamon Rolls", main, None,
             ["cinnamon roll", "sugar frosting"])
    ]

    breakfast_side_ls = [
        Item("Applesauce Cup", side, None,
             ["applesauce", "cinnamon"]),
        Item("Choice of Seasonal Fruit", side, None,
             ["apple", "banana", "pear", "orange"])
    ]

    # same drinks for both breakfast and lunch
    drink_ls = [
        Item("1% White Milk", drink, None, None),
        Item("Fat Free White Milk", drink, None, None),
        Item("Fat Free Chocolate Milk", drink, None, None),
        Item("Fat Free Strawberry Milk", drink, None, None),
        Item("Orange Juice", drink, None, None),
        Item("Apple Juice", drink, None, None)
    ]

    # two menus per day, breakfast and lunch
    # one main per menu
    # sides and drinks all available

    # create our single school district
    SchoolDistrict = apps.get_model("Lapp", "SchoolDistrict")
    temp_district = SchoolDistrict.objects.create(name=district)

    # create the schools in the district
    for school in schools:
        temp_school = temp_district.school_set.create(name=school)

        # create pickup times
        timeAM = str(random.randint(7, 10)) + ":00AM"
        timePM = str(random.randint(2, 6)) + ":00PM"
        temp_school.time_set.create(name=timeAM)
        temp_school.time_set.create(name=timePM)

        # create menus for each school
        for day in range(5):
            # breakfast menu
            temp_breakfast = temp_school.menu_set.create(name=breakfast)

            # ### BREAKFAST ### #
            num = random.randint(0, len(breakfast_main_ls) - 1)
            temp_item = temp_breakfast.meal_set.create(name=breakfast_main_ls[num].name,
                                                       description=breakfast_main_ls[num].description,
                                                       prep=breakfast_main_ls[num].prep)

            # breakfast main course ingredients
            for ingredient in breakfast_main_ls[num].ingredient_ls:
                temp_item.ingredient_set.create(name=ingredient)

            # breakfast sides
            for item in breakfast_side_ls:
                temp_item = temp_breakfast.meal_set.create(name=item.name,
                                                           description=item.description,
                                                           prep=item.prep)
                for ingredient in item.ingredient_ls:
                    temp_item.ingredient_set.create(name=ingredient)

            # breakfast drink
            for item in drink_ls:
                temp_breakfast.meal_set.create(name=item.name, description=item.description, prep=item.prep)

            # ### LUNCH ### #
            temp_lunch = temp_school.menu_set.create(name=lunch)

            # lunch main course
            num = random.randint(0, len(lunch_main_ls) - 1)
            temp_item = temp_lunch.meal_set.create(name=lunch_main_ls[num].name,
                                                   description=lunch_main_ls[num].description,
                                                   prep=lunch_main_ls[num].prep)

            # lunch main course ingredients
            for ingredient in lunch_main_ls[num].ingredient_ls:
                temp_item.ingredient_set.create(name=ingredient)

            # lunch sides
            for item in lunch_side_ls:
                temp_item = temp_lunch.meal_set.create(name=item.name,
                                                       description=item.description,
                                                       prep=item.prep)
                for ingredient in item.ingredient_ls:
                    temp_item.ingredient_set.create(name=ingredient)

            # lunch drink
            for item in drink_ls:
                temp_lunch.meal_set.create(name=item.name, description=item.description, prep=item.prep)


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


# this holds menu information for two times
class TimeObj:
    def __init__(self, time_id, name):
        self.id = time_id
        self.name = name
        self.time_ls = []

    def __str__(self):
        return self.name


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
        self.num_time = 1

        district = 'district'
        school = 'school'
        menu = 'menu'
        item = 'item'
        description = 'description goes here'
        prep = 'prep goes here'
        ingr = 'ingr'
        time1 = '0:00 AM'
        time2 = '0:00 PM'

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

            # create times for each school
            for k in range(self.num_time):
                time1 = str(i) + ':' + str(j) + str(k) + 'AM'
                temp_time1 = temp_school.time_set.create(name=time1)
                time2 = str(i) + ':' + str(j) + str(k) + 'PM'
                temp_time2 = temp_school.time_set.create(name=time2)

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

        # set up a user & log in
        self.client = Client()
        self.credentials = {
            'username': 'george',
            'password': 'secret',
            'email': 'email@gmail.com'}
        self.user = MyUser.objects.create(username=self.credentials['username'], email=self.credentials['email'],
                                          password=self.credentials['password'])
        user = authenticate(username=self.credentials['username'], password=self.credentials['password'])
        if user:
            self.client.login(username=self.credentials['username'], password=self.credentials['password'])

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
            'time_ls': [],
            'error': None
        }

        for school in School.objects.all():
            temp_school = SchoolObj(school.id, school.name)
            meal_context['school'] = temp_school

            if school.time_set.exists():
                for time in school.time_set.all():
                    temp_time = MenuObj(time.id, time.name)
                    meal_context['time_ls'].append(temp_time)

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
