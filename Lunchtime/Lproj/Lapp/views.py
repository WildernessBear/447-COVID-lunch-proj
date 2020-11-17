from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import School  # , Menu, Meal, SchoolDistrict


def index(request):
    return render(request, 'Lapp/index.html')


@login_required
def special():  # Removed: request
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def schools_menu(request):
    return render(request, 'Lapp/schools.html', {})


@login_required
def meals_menu(response, sch_id):
    # this dictionary will be passed to the template
    context = {
        'school': '',
        'menu_ls': [],
        'error': None
    }

    if School.objects.filter(pk=sch_id).exists():

        school = School.objects.get(pk=sch_id)

        context['school'] = school.name

        print(school.name)

        if school.menu_set.exists():
            for menu in school.menu_set.all():
                temp_menu = MenuObj(menu.name)

                for item in menu.meal_set.all():
                    temp_meal = MealObj(item.name, item.description)

                    temp_menu.meal_ls.append(temp_meal)

                context['menu_ls'].append(temp_menu)

        else:
            context['menu_ls'].append('menu does not exist')
            context['error'] = 'menu does not exist'

    else:
        context['school'] = 'school does not exist'
        context['error'] = 'school does not exist'

    return render(response, 'Lapp/meals.html', context)


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


# this holds menu information for a single menu
class MenuObj:
    def __init__(self, name):
        self.name = name
        self.meal_ls = []

    def __str__(self):
        return self.name


# this holds information for a single meal
class MealObj:
    def __init__(self, name, description):
        self.name = name
        self.description = description
