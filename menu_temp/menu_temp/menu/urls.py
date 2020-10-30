from django.conf.urls import url
from django.urls import path
from django.urls import include, path
from . import views

#app_name = 'dappx'

urlpatterns = [
    path('menu/<int:id>', views.menu, name='menu'),
    #url(r'^menu/$', views.menu, name='menu'),
    #path('', views.menu, name='menu'),
]