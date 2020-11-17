from django.conf.urls import url
from django.urls import path  # Removed: include,
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
]
