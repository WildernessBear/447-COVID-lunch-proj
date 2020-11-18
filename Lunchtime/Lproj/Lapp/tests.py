import os
import unittest
import time
from django.test import TestCase
from django.test import LiveServerTestCase
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Create your tests here.

HOMEPAGE = 'http://localhost:8000'

# USER_NAME = os.environ['USER_NAME']
# USER_PASSWORD = os.environ['USER_PASSWORD']


class FunctionalTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        # self.browser.implicitly(3)

    def tearDown(self):
        self.browser.quit()

    # from the homepage, navigate to the Registration page, create a valid user
    # then navigate to Login page. Log in using that valid user
    def test_valid_user_login(self):
        self.browser.get(HOMEPAGE)
        assert 'The Lunch Project' in self.browser.title
        # Register a user
        self.browser.find_element_by_link_text('Register').click()

        username = self.browser.find_element_by_name('username')
        username.clear()
        username.send_keys('name')

        password = self.browser.find_element_by_name('password')
        password.clear()
        password.send_keys('password')

        email = self.browser.find_element_by_name('email')
        email.clear()
        email.send_keys('name@example.com')

        self.browser.find_element_by_name('RegistrationButton').click()

        # verify that the user has been logged in
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'Registered'))
        )
        print(element)
        if (element == 'Thank you for registering!'):
            print("Pass: Registered correctly")
        else:
            print("Fail: Problem registering")

        # Log that user in
        self.browser.find_element_by_link_text('Login').click()

        username = self.browser.find_element_by_name('username')
        username.clear()
        username.send_keys('name')

        password = self.browser.find_element_by_name('password')
        password.clear()
        password.send_keys('password')

        self.browser.find_element_by_name('LoginButton').click()

        # verify that the user has been logged in
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'LoggedIn'))
        )
        print(element)
        if (element == 'Hello name'):
            print("Pass: Logged in correctly")
        else:
            print("Fail: Problem logging in")

        # self.browser.find_element_by_partial_link_text('Home')
        time.sleep(2)


        # finds elements in the nav bar, but just selects the first one: ie Admin
        # self.browser.find_element_by_class_name('navbar-link').click()


    # def test_login_is_good(self):
        # self.browser.get(HOMEPAGE)

# if __name__ == '__main__':
#   unittest.main()
