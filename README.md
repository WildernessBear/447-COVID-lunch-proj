# 447-COVID-lunch-proj

Now in a more stable state. A new user may register and log in, an existing user may log in, and an admin may log in either at the site itself or to the admin page. A user, once logged in, can check a FAQ page, update their profile with their student's dietary restrictions, or can select their school and find that week's menu (with included ingredient lists), pick-up location and time, and an option to register for e-mail reminders for pick-ups.

## To run the program:
1. Navigate to `Lunchtime/Lproj/` on your command line
2. Enter the command `python manage.py runserver` (some terminals will need the command `python3`)
3. Navigate to the local link in your browser (http://127.0.0.1:8000/)

## Dependencies:
- python3
- asgiref == 3.2.10
- Django == 3.1.2
- pytz == 2020.1
- selenium == 3.141.0
- sqlparse == 0.3.1

## To run the tests:
Tests using Selenium:
We're using Firefox as the browser, be aware.
Requires geckodriver, download from Mozilla's github (https://github.com/mozilla/geckodriver/releases) the appropriate release for your system.
Unzip and put geckodriver.exe in `Lunchtime/Lproj/`, alongside manage.py
Selenium will now be functional!
To run:
1. Navigate to `Lunchtime/Lproj/`
2. Enter the command `python manage.py test Lapp.tests`
These tests are for the general functionality of the website as a whole

Menu tests:

1. Navigate to `Lunchtime/Lproj/`
2. Enter the command `python manage.py test Lapp.test_menu`
This test will make sure the databases for lunches are set up properly.

FAQ tests:
1. Navigate to `Lunchtime/Lproj/`
3. Enter the command `python manage.py test Lapp.faq`
