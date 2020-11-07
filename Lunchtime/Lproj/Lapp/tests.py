import os
import unittest
from django.test import TestCase
from django.test import LiveServerTestCase
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

HOMEPAGE = 'http://localhost:8000'

#USER_NAME = os.environ['USER_NAME']
#USER_PASSWORD = os.environ['USER_PASSWORD']


class FunctionalTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        # self.browser.implicitly(3)

    def tearDown(self):
        self.browser.quit()

    def test_homepage_is_good(self):
        self.browser.get(HOMEPAGE)
        # self.assertIN('The Lunch Project', self.browser.title)
        # assert self.browser.title == 'The Lunch Project'
        assert 'The Lunch Project' in self.browser.title


    def test_login_is_good(self):
        self.browser.get(HOMEPAGE)
        # self.assertIN('The Lunch Project', self.browser.title)

# if __name__ == '__main__':
#   unittest.main()
