from django.test import TestCase
from .models import SchoolDistrict, School, Menu, Meal

# FOR DATABASE TESTS: classes should be subclasses django.test.TestCase
# ONLY FOR NON-DATABASE TESTS: classes subclasses of unittest.TestCase

# menu models test case
# makes sure the databases associated with models are organized correctly
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


    def test_organization_of_db(self):
        for x in SchoolDistrict.objects.all():
            print(x.name)
            for y in x.school_set.all():
                print('\t', y.name)

        for district in SchoolDistrict.objects.all():
            for school in district.school_set.all():
                self.assertEqual(district.id, school.district.id)



