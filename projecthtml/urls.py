#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""projecthtml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin,auth
from django.contrib.auth import urls


admin.site.site_title='Python'
admin.site.index_title='使用者後台'
admin.site.site_header="Python教學網站"

auth.forms.username_field="帳號"



from htmlapp import views as html_views ,part1_views ,beginner_views 


urlpatterns = [
    url(r'^$',html_views.index,name='index'),

    url(r'^index',html_views.index,name='index'),
    url(r'^login',html_views.login,name='login'),
    url(r'^logout',html_views.logout,name='logout'),
    url(r'^register',html_views.register,name='register'),
    url(r'^dess',html_views.dess,name='dess'),
    url(r'^setting',html_views.setting,name='setting'),
    url(r'^change_password',html_views.change_password,name='change_password'),
    url(r'^course',html_views.course,name='course'),
    url(r'^null_course',html_views.null_course,name='null_course'),
    
    url(r'^accounts/login',html_views.login_error,name='error'),
    url(r'^python_part(?P<part>\d)',part1_views.python_part1),


    
    url(r'^python_beginner(?P<part>\d)_Ch(?P<ch>\d)_synopsis',beginner_views.python_beginner),
    url(r'python_beginner(?P<part>\d)_Ch(?P<ch>\d)_(?P<num>\d+)',beginner_views.beginner_course),
    

    url(r'^part(?P<part>\d)_Ch(?P<c>\d)_synopsis',part1_views.part1_synopsis),
    url(r'^part(?P<part>\d)_Ch(?P<ch>\d)_(?P<num>\d+)',part1_views.part1),
 
 
    
    url(r'^user',html_views.user,name='user'),
    
    url(r'^admin/', admin.site.urls),
]
