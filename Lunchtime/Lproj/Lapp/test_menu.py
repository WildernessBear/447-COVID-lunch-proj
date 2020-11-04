from django.test import TestCase
from .models import SchoolDistrict, School, Menu, Meal

# FOR DATABASE TESTS: classes should be subclasses django.test.TestCase
# ONLY FOR NON-DATABASE TESTS: classes subclasses of unittest.TestCase

# menu models test case
# makes sure the databases associated with models are organized correctly
# also prints out contents of temporary databases
# breakdown of temp databases:
#   10 districts
#   each district has 10 schools
#   each school has 2 menus
#   each menu has 3 items
class MenuModelsTestCase(TestCase):
    def setUp(self):
        self.num_districts = 10
        self.num_schools = 10
        self.num_menus = 2
        self.num_items = 3

        district = 'district'
        school = 'school'
        menu = 'menu'
        item = 'item'
        description = 'description goes here'

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
                        temp_menu.meal_set.create(name=item, description=description)
                        item = 'item'


    def test_organization_of_db(self):
        for i in SchoolDistrict.objects.all():
            print(i.name)
            for j in i.school_set.all():
                print('\t', j.name)
                for k in j.menu_set.all():
                    print('\t\t', k.name)
                    for m in k.meal_set.all():
                        print('\t\t\t', m.name, ': ', m.description)

        for district in SchoolDistrict.objects.all():
            for school in district.school_set.all():
                self.assertEqual(district.id, school.district.id)
                for menu in school.menu_set.all():
                    self.assertEqual(school.id, menu.school.id)
                    for item in menu.meal_set.all():
                        self.assertEqual(menu.id, item.menu.id)



