"""Lproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # Removed: , include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# noinspection PyUnresolvedReferences
from Lapp import views

urlpatterns = [
    # path('', include(('Lapp.urls', 'Lapp'), namespace='Lapp'))
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^Lapp/', include('Lapp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('menu/<int:sch_id>', views.meals_menu, name='menu'),
    path('menu/meal_page/<int:item_id>', views.meal_page, name='meal_page'),
    path('menu/menu_page/<int:item_id>', views.menu_page, name='menu_page'),
    path('simpleemail/<emailto>/<int:sch_id>', views.send_simple_email,
         name='send_simple_email'),
    path('faq/', views.faq, name='faq'),
    path('profile/', views.update_profile, name='profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
