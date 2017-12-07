#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from django.db import models
from django.contrib import admin
from jsonfield import JSONField
import collections



class course4_attribute(models.Model):
    lesson_name=models.CharField(max_length=30 ,default="")
    lesson_introduction=models.TextField(max_length=255 ,default="")
    lesson=models.CharField(max_length=30 ,default="")
    user_id=models.ManyToManyField(User,default="")
    def __str__(self):
        return self.lesson
        
        
class course4_detail(models.Model):
    
    num=models.CharField(max_length=20,default='')
    ch=models.CharField(max_length=20 , default='')
    part=models.CharField(max_length=20 , default='')
    name=models.CharField(max_length=20 , default='')
    comparison = JSONField(null=True, blank=True,default="")

    answer=models.TextField(max_length=10000,default="")
    course_attribute=models.ForeignKey(course4_attribute(),default='')

    def __str__(self):
        return str(self.name)+str(self.part)+'_Ch'+ str(self.ch) + '_' + str(self.num)        

class course_user(models.Model):
    user= models.ForeignKey(User)
    code=models.TextField(max_length=1000,default="")
    coursename=models.CharField(max_length=20,default="")
    correct=models.BooleanField(default=False)
    lesson=models.ForeignKey(course4_attribute(),default="")


class course4(models.Model):
    content=models.TextField(max_length=1000,default="")
    description=models.TextField(max_length=1000,default="")
    ch=models.ForeignKey(course4_detail(),default="")
    variable=models.TextField(max_length=10000,default="")
    course_attribute_id=models.ForeignKey(course4_attribute(),default="")

    

class Introduction(models.Model):
    sef =models.TextField(max_length=255)
    user= models.ForeignKey(User)
    lesson=models.ManyToManyField(course4_attribute, blank=True)
    
