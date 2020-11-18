# 447-COVID-lunch-proj

Minimal functionality now exists. A new user may register and log in, an existing user may log in, and an admin may log in either at the site itself or to the admin page.

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
Menu tests:

1. **IMPORTANT**: MenuTemplatesTestCase does not work if user login is required. Go to views and comment out `@login_required` above the following lines:
    ```python
    def schools_menu(request):
    def meals_menu(response, sch_id):
    def meal_page(response, item_id):```
2. Navigate to `Lunchtime/Lproj/`
3. Enter the command `python manage.py test Lapp.test_menu`
This test will make sure the databases for lunches are set up properly.
