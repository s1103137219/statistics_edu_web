#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import *
from django.contrib import auth
import collections




class course_userAdmin(admin.ModelAdmin):
    list_display = ('user','correct','code','coursename','lesson')

    
class Introductionadmin(admin.ModelAdmin):
    list_display = ('user','sef')


class course4_detailAdmin(admin.ModelAdmin):
    list_display=('name','part','ch','num','answer','comparison','course_attribute')
    

class course4Admin(admin.ModelAdmin):
    list_display=('ch','course_attribute_id')
    
class course4_attributeAdmin(admin.ModelAdmin):
    list_display=('lesson','lesson_introduction','lesson_name')
    
admin.site.register(course_user,course_userAdmin)
admin.site.register(Introduction,Introductionadmin)
admin.site.register(course4,course4Admin)
admin.site.register(course4_detail,course4_detailAdmin)
admin.site.register(course4_attribute,course4_attributeAdmin)
admin.site.register(auth.models.Permission)
