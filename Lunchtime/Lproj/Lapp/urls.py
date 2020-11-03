from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'Lapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^loc_time_menu/$', views.loc_time_menu, name='loc_time_menu'),
]
