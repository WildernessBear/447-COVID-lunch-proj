# 447-COVID-lunch-proj

Minimal functionality now exists, a new user may register and log in, an existing user may log in, an admin may log in either at the site itself or to the admin page.

## To run the program:
1. Navigate to `Lunchtime/Lproj/mysite` on your command line
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
Menu tests:
1. Navigate to `Lunchtime/Lproj/`
2. Enter the command `python manage.py test Lapp.test_menu`

