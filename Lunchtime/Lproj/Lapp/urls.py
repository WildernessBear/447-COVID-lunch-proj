from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# SET THE NAMESPACE!
app_name = 'Lapp'
# Be careful setting the name to just /login; use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^meals_menu/$', views.meals_menu, name='meals_menu'),
    url(r'^schools_menu/$', views.schools_menu, name='schools_menu'),
    path('menu/<int:sch_id>', views.meals_menu, name='menu'),
    path('menu/meal_page/<int:item_id>', views.meal_page, name='meal_page'),
    path('faq/', views.faq, name='faq'),
    path('profile/', views.update_profile, name='profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),

]
