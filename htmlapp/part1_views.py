#!/usr/bin/env python
# -*- coding: utf-8 -*-
from htmlapp.course import *
from htmlapp.models import *
import re


@login_required
def setuser(request):
    user_sta=course4_attribute.objects.filter(user_id=request.user.id)
    lesson_sta=course4_attribute.objects.all()
    lesson_sta=[lesson_sta[x].lesson_name for x in range(len(lesson_sta))]
    user_sta=[user_sta[x].lesson_name for x in range(len(user_sta))]
    lesss=''
    for x in range(len(user_sta)):
        lesss=lesss+','+user_sta[x]
    
    return lesss
    
    
@login_required
def python_part1(request):

    return render(request,'./course/python_part1/python_part1.html')

    
@login_required
def part1_synopsis(request,part=1,c=1):
    les="part%s_Ch1_synopsis"%(part)
    les_course=setuser(request)
    les_c=les_course.find(les)
    if les_c <0 :
        return HttpResponseRedirect('/null_course/')
        
    return render(request,'./course/python_part'+part+'/Ch'+c+'/part'+part+'_Ch'+c+'_synopsis.html',locals())




@login_required
def part1(request,part=1,ch="1",num="1"):
    webid="#code"
    les="part%s_Ch1_synopsis"%(part)
    les_course=setuser(request)
    les_c=les_course.find(les)
    if les_c <0 :
        return HttpResponseRedirect('/null_course/')
    
           
    les=course4_attribute.objects.get(lesson_name=les)
    #查詢當前課程的網址(如 prat1_Ch1_1) 是否存在使用者
    coname="part%s_Ch%s_%s"%(part,ch,num)
    with connection.cursor() as cursor:
         cursor.execute('SELECT * FROM htmlapp_course_user WHERE user_id=%s and coursename=%s',[request.user.id,coname])
         row = cursor.fetchone()
    br=bool(row)
    
    #如果存在先更新資料 不存在回傳空值 到 POST 判斷
    if bool(row) ==True:
       courseuser=course_user.objects.get(user_id=str(request.user.id),coursename=coname,lesson=les)
       coding = courseuser.code
       courseuser.save()
    elif bool(row) ==False:
       courseuser=course_user(user_id=str(request.user.id),code="",coursename=coname,lesson=les) #如果沒有創立資料
       courseuser.save()
    
    
       
    if request.method == 'POST': # 傳送方式POST
       
        tes=request.POST['tes']  # 隱藏文字方塊
        code=open('code.py','w') # 讀檔

        
        if bool(row) != True:     #使用者有無進入課程
           
           cour=course_user(user_id=str(request.user.id),code=tes,coursename=coname,lesson=les) #如果沒有創立資料
           cour.save()
        elif bool(row) == True:
           courseuser=course_user.objects.get(coursename=coname,user_id=str(request.user.id),lesson=les) #查詢使用者
           courseuser.code=tes
           courseuser.save()
        var=course4.objects.get(ch=int(part)+int(ch)+int(num)) #課程第幾課 第幾節
        var=var.variable   # 放變數
        
        # 是pyplot 有無使用 "find" 查詢 pyplot在不在
        tf=tes.find('plt')
        
        deferror='def'
        iferror='if'
        tx=len(tes)
        ifer=''
        #如果在 加入 引用圖形的 .use('agg')
        if tf >= 0:
            code.write("import matplotlib;matplotlib.use('agg');"+"from function import *"+";\n"+tes+"\nmatplotlib.pyplot.savefig('htmlapp/static/image/plot.svg')")
        else:
            code.write("from function import *;\n"+tes)
            
                   
            os.system("sudo rm htmlapp/static/image/plot.svg") #如果沒有 移除圖片 不加入 引用圖形的 .use('agg')
        code.close()
        osys=os.system('./run.sh > Anser')# Linux管理者 權限 執行 python3.5版本 的 code.py "> Anser"表示存檔至 Anser

        mng=""
        mngtrue=""
        #打開答案 讀取 放入 html
        anse=open('Anser','r')   
        ans=anse.read()
        
        anse.close()
        commng=" 答案中缺少 "
        comm=[]
        com=[]
        anserr=ans.find('Error')
        if anserr >= 0:
           os.system("sudo rm htmlapp/static/image/plot.svg")
           mng="變數或套件錯誤"
        
        
        comparison=course4_detail.objects.get(name='Part',part=part,ch=ch,num=num)
        comparison=comparison.comparison
        if 'anser' in request.POST:
            an='anser'
        if bool(comparison) == True:
            compar=[y for x,y in comparison.items()]
            for x in range(len(compar)):
                comm.append(tes.find(compar[x]) >= 0)
                if comm[x] == False:
                    com.append(compar[x])
            comlen=len(com)
            correct=course_user.objects.get(coursename=coname,user_id=request.user.id)
            if comlen == 0 :
               correct.correct=True
               correct.save()
            elif comlen != 0 :
               correct.correct=False
               correct.save()
               os.system("sudo rm htmlapp/static/image/plot.svg")
               mng="變數或套件錯誤"
               for x in range(comlen):
                   if x == comlen-1:
                      commng=commng+" "+com[x]
                   else:
                      commng=commng+" "+com[x]+","
        else:
            commng=""
        
        
        
    elif request.method == 'GET':
        if 'help' in request.GET:
            hel='help'
            helpmeg=course4_detail.objects.get(name='Part',part=part,ch=ch,num=num)
            helpmes=helpmeg.answer
        elif 'help2' in request.GET:
            hel='help2'
    else:
        os.system("sudo rm htmlapp/static/image/plot.svg")
    

      

    return render(request,'./course/python_part'+part+'/Ch'+ch+'/part'+part+'_Ch'+ch+'_'+num+'.html',locals())


        
