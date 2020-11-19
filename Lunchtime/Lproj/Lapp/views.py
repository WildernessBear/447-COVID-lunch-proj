from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import School, Meal, SchoolDistrict  # , Time, Menu

# this holds info for a single school
class SchoolObj:
    def __init__(self, school_id, name):
        self.id = school_id
        self.name = name


# this holds menu information for a single menu
class MenuObj:
    def __init__(self, menu_id, name):
        self.id = menu_id
        self.name = name
        self.meal_ls = []

    def __str__(self):
        return self.name


# this holds menu information for two times
class TimeObj:
    def __init__(self, time_id, name):
        self.id = time_id
        self.name = name
        self.time1_ls = []
        self.time2_ls = []

    def __str__(self):
        return self.name


# this holds information for a single meal
class MealObj:
    def __init__(self, meal_id, name, description, prep):
        self.id = meal_id
        self.name = name
        self.description = description
        self.prep = prep
        self.ingredient_ls = []


def index(request):
    return render(request, 'Lapp/index.html')


@login_required
def special():  # Removed: request
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


#@login_required
def schools_menu(request):
    context = {
        'school_ls': []
    }

    all_schools = School.objects.all()
    for school in all_schools:
        temp_school = SchoolObj(school.id, school.name)
        context['school_ls'].append(temp_school)

    return render(request, 'Lapp/schools.html', context)


#@login_required
def meals_menu(response, sch_id):
    # this dictionary will be passed to the template
    context = {
        'school': '',
        'menu_ls': [],
        'time1_ls': [],
        'time2_ls': [],
        'error': None
    }

    if School.objects.filter(pk=sch_id).exists():

        school = School.objects.get(pk=sch_id)
        temp_school = SchoolObj(school.id, school.name)

        context['school'] = temp_school

        if school.time_set.exists():
            for time1 in school.time_set.all():
                temp_time1 = MenuObj(time1.id, time1.name)
                context['time1_ls'].append(temp_time1)

            for time2 in school.time_set.all():
                temp_time2 = MenuObj(time2.id, time2.name)
                context['time2_ls'].append(temp_time2)

        else:
            context['time1_ls'].append('time1 does not exist')
            context['time2_ls'].append('time2 does not exist')
            context['error'] = 'time does not exist'

        if school.menu_set.exists():
            for menu in school.menu_set.all():
                temp_menu = MenuObj(menu.id, menu.name)

                for meal in menu.meal_set.all():
                    temp_meal = MealObj(meal.id, meal.name, meal.description, meal.prep)

                    if meal.ingredient_set.exists():
                        for ingredient in meal.ingredient_set.all():
                            temp_meal.ingredient_ls.append(ingredient.name)

                    temp_menu.meal_ls.append(temp_meal)

                context['menu_ls'].append(temp_menu)

        else:
            context['menu_ls'].append('menu does not exist')
            context['error'] = 'menu does not exist'

    else:
        context['school'] = 'school does not exist'
        context['error'] = 'school does not exist'

    return render(response, 'Lapp/meals.html', context)


#@login_required
def meal_page(response, item_id):
    context = {
        'meal': '',
        'error': None
    }

    meal = Meal.objects.get(pk=item_id)
    temp_meal = MealObj(meal.id, meal.name, meal.description, meal.prep)

    if meal.ingredient_set.exists():
        for ingredient in meal.ingredient_set.all():
            temp_meal.ingredient_ls.append(ingredient.name)

    context['meal'] = temp_meal

    return render(response, 'Lapp/meal_page.html', context)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors, )
    else:
        user_form = UserForm()
    return render(request, 'Lapp/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Lapp/login.html', {})
