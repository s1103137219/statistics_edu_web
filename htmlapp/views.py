#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.contrib import auth
from django.http import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Count
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from htmlapp.forms import loginform 
from htmlapp.models import *
from django.views.decorators.csrf import csrf_exempt  
import smtplib
import random


def csrf_failure(request, reason=""):
    mng="請勿不當操作。"
    return render_to_response('404.html',locals())

def null_course(request):
    mng="這是沒有選取過的課程！"
    return render(request,'nullcourse.html',locals())


def index(request):
    
    
    return render(request, 'index.html',locals())

def dess(request):
    return render(request,'test.html')

@csrf_exempt
def login(request):
     if request.method == 'POST':
        form = loginform(request.POST)
        mng=""
        email = request.POST['email']
        passd = request.POST['passd']
        user = auth.authenticate(username=email , password=passd)
        if user is not None and user.is_staff:
            auth.login(request, user)
            mng="登入成功"
            return HttpResponseRedirect('/setting/',locals())
        else:
            mng="帳號或密碼錯誤"
            return render(request,'login.html',locals())
        
    
        
     else:
        form = loginform()
     
     if request.method == 'GET':
         unpassword='unpassword'
         user_email=User.objects.all()
         user_email=[user_email[x].email for x in range(len(user_email))]
         email=request.GET.get('email')
         confirm=0
         bool_email=bool(email)
         if bool_email == True:
            for x in range(len(user_email)):
                if user_email[x] != email:
                   confirm=confirm+0
                else:
                   confirm=confirm+1
         if confirm == 1:
            rand1 = [chr(random.randint(97, 122)) for x in range(4) ]
            rand2 = [chr(random.randint(65, 90)) for x in range(4)]
            rand=""
            for x in range(len(rand1)):
                rand=rand+rand1[x]+rand2[x]
            user_password=User.objects.get(email=email)
            user_password.set_password(rand)
            user_password.save()
            into='請記住新的密碼：'+rand+'\n若要修改請至 https://projecthtml-theleaves.c9users.io/ 登入後修改' 
            gmail_user = 'pythonbeginnercourse@gmail.com'
            gmail_pwd = '3ajilojl'
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(gmail_user, gmail_pwd)
            fromaddr = "pythonbeginnercourse@gmail.com"
            toaddrs = [email]
            msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (fromaddr, ", ".join(toaddrs), 'Python教學網站'))
            smtpserver.sendmail(fromaddr, toaddrs,msg.encode('utf-8')+into.encode('utf-8'))
            smtpserver.quit()
             
     return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def change_password(request):
    if request.method == "POST":
        password=User.objects.get(id=request.user.id)
        change_password=request.POST['passd']
        confirm_password=request.POST['passd2']
        if change_password == confirm_password :
            password.set_password(change_password)
            password.save()

    return render(request,'change_password.html',locals())

def register(request):
    user_email=User.objects.all()
    
    if request.method == 'GET' && 'confirm' in request.GET:

           acc_confirm = 0
           email_confirm = 0
           bool_register=''
           utest=User.objects.all()
           user_acc=[utest[x].username for x in range(len(utest))]
          
           confirm='confirm'
           user_email=[user_email[x].email for x in range(len(user_email))]
           email=request.GET.get('email')
           acc=request.GET.get('acceunt')
           for x in range(len(user_acc)):
               if user_acc[x] == acc:
                   acc_confirm=acc_confirm+1
               #else:
                #   acc_confirm=acc_confirm+1
           for x in range(len(user_email)):
               if user_email[x] == email:
                   email_confirm=email_confirm+1
               #else:
                #   email_confirm=email_confirm+1
           if acc_confirm ==0 and email_confirm ==0: 
              password=request.GET.get('passd')
              password2=request.GET.get('passd2')
              if password == password2 and password != '' and password2 != '':
                 bool_register=True
                 user_add=User.objects.create(username=acc,email=email,password=password,is_staff=True)
                 user_add.set_password(password)
                 user_add.save()
           else:
              bool_register=False
             
    return render(request, 'register.html',locals())

@login_required
def setting(request):

    row=course4_attribute.objects.filter(user_id=str(request.user.id))   
    coursebool=bool(row)
    if coursebool != False:
       test=course4_attribute.objects.filter(user_id=str(request.user.id))
       testa=[x for x in test]
       testc=len(testa)
       if request.method =="GET" && testc != 0:
             for x in range(len(testa)):
                 if str(testa[x].lesson_name)+"_cancel" in request.GET:
                    b=str(testa[x].lesson_name)
                    testc=testc-1
                    course=course4_attribute.objects.get(lesson_name=b)
                    course.user_id.remove(int(request.user.id)) # add 新增 remove 刪除
                    b=str(testa[x].lesson_name)+"_cancel"
                    
                    course.save()
           
    
        
    return render(request, 'set.html',locals())

@login_required
def course(request):
    bb= "test"
    
    if request.method =='GET':
        lesson=course4_attribute.objects.all()
        a=[x for x in lesson]
        for x in range(len(a)):
            if str(a[x].lesson_name) in request.GET:
               b=str(a[x].lesson_name)
       
               course=course4_attribute.objects.get(lesson_name=b)
               course.user_id.add(int(request.user.id)) # add 新增 remove 刪除
               course.save()
            elif str(a[x].lesson_name)+"_cancel" in request.GET:

               b=str(a[x].lesson_name)+"_cancel"
               
    return render(request, 'course.html',locals())
    
    
    
    



@login_required
def user(request):
    lan=""

    lesson=course4_attribute.objects.filter(user_id=str(request.user.id)).order_by('id')
    a=[lesson[x].id for x in range(len(lesson)) ]
    
    tcourse= course4_detail.objects.values('course_attribute_id').annotate(dcount=Count('course_attribute_id')).order_by('course_attribute_id')
    cs=course_user.objects.values('lesson_id').annotate(dcount=Count('coursename')).filter(user_id=str(request.user.id),correct=True).order_by('lesson_id')
    tc=[]
    tt=[]
    tct=[]
    
    for x in range(len(tcourse)):
        for y in range(len(a)):
            if tcourse[x]['course_attribute_id'] == a[y] :
                tt.append({"課程":lesson[y].lesson,"課程數量":tcourse[x]['dcount']})
                
    for x in range(len(cs)):
        for y in range(len(a)):
            if cs[x]['lesson_id'] == a[y] :
                tc.append({"課程":lesson[y].lesson,"課程答對數":cs[x]['dcount']})
                
    for x in range(len(tt)):
        for y in range(len(tc)):
            if tt[x]['課程'] == tc[y]['課程']:
                
                tct.append({"課程":tc[y]['課程'],"百分比":(round(round(tc[y]['課程答對數']/tt[x]['課程數量'],4)*100,2))})
           

     
    with connection.cursor() as cursor:
         cursor.execute('SELECT count(coursename) FROM htmlapp_course_user WHERE user_id=%s and correct=%s group by lesson_id',[request.user.id,True])
         row = cursor.fetchone()    
         
    
    with connection.cursor() as cursor:
             cursor.execute('SELECT * FROM htmlapp_Introduction WHERE user_id=%s ',[request.user.id])
             row2 = cursor.fetchone()
    ##修改個人資料
    if request.method == 'GET':
        if 'lastbtn' in request.GET:
            lan='lastbtn'
            lastn=request.GET.get("lastname")
            user=User.objects.get(username=request.user.username)
        elif 'lastbtn2' in request.GET:
            lan='lastbtn2'
            lastn=request.GET.get("lastname")
            user=User.objects.get(username=request.user.username)
            user.last_name=lastn
            user.save()

        if 'ebtn' in request.GET:
            lan='ebtn'
            user=User.objects.get(username=request.user.username)
            
        elif 'ebtn2' in request.GET:
            lan='ebtn2'
            en=request.GET.get("ename")
            user=User.objects.get(username=request.user.username)
            user.email=en
            user.save()   
            
        if 'firstbtn' in request.GET:
            lan='firstbtn'
            user=User.objects.get(username=request.user.username)
        elif 'firstbtn2' in request.GET:
            lan='firstbtn2'
            fristn=request.GET.get("firstname")
            user=User.objects.get(username=request.user.username)
            user.first_name=fristn
            user.save() 
        
        ##若無介紹欄位創建空欄之後 每次進入都能夠修改    
        
        if bool(row2) != True:
            arean=request.GET.get("areaname")
            cour=Introduction(user_id=str(request.user.id),sef="")
            cour.save()
        elif bool(row2) == True :
             fuser=Introduction.objects.get(user_id=request.user.id)           
             if 'areabtn' in request.GET:
                lan='areabtn'
                fuser=Introduction.objects.get(user_id=request.user.id)           

             elif 'areabtn2' in request.GET:
                 lan='areabtn2'
                 arean=request.GET.get("areaname")
                 fuser=Introduction.objects.get(user_id=request.user.id)
                 fuser.sef=arean
                 fuser.save()
           
    return render(request,'./userdata/userdata.html',locals())


def login_error(request):
    mng="請勿不當操作。"
    return render(request,'404.html',locals())
