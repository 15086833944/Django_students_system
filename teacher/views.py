from django.shortcuts import render
from django.shortcuts import redirect
from db import models

# Create your views here.


# """教师登录页面"""
def teacher_login(request):
    error_msg=""
    count = 0
    if request.method == "POST":
        user = request.POST.get("tname", None)
        pwd = request.POST.get("tpwd", None)
        all_info = models.Teacher.objects.all().values("tname", "tpwd","tid")
        for x in all_info:
            if x["tname"] == user:
                if x["tpwd"] == pwd:
                    rep=render(request,"teacher_main_page.html",{"user_name":user})
                    rep.set_cookie("tid",x["tid"])
                    count += 1
                    return rep
        if count == 0:
            error_msg = "您输入的账号或密码错误！！"
        return render(request, "teacher_login.html", {'error_msg': error_msg})
    return render(request, 'teacher_login.html', {'error_msg': error_msg})


# 教师查询个人信息
def teacher_self_info(request):
    uid=request.COOKIES.get("tid")
    print(uid)
    if not uid:
        return render(request,"teacher_login.html")
    # 查找该教师的信息并发送至页面
    all_info = models.Teacher.objects.values()
    for x in all_info:
        if x["tid"]==int(uid):
            if not x["tsex"]:
                msg="女"
            else:
                msg = "男"
            if x["tquestion"]=="":
                tishi="您还没有密保问题,赶紧去设置吧O(∩_∩)O~"
            else:
                tishi=x["tquestion"]
            dit={
                "tid":x["tid"],
                "question":tishi,
                "tname":x["tname"],
                "tsex":msg,
                "tpost":x["tpost"],
                "tphone":x["tphone"],
                "user_name":x["tname"]
            }
            return render(request, 'teacher_self_info.html',dit)
    return render(request, 'teacher_self_info.html')


# 教师修改个人密码
def teacher_changepwd(request):
    error_msg=""
    change_info=""
    msg=""
    uid = request.COOKIES.get("tid")
    if not uid:
        return render(request, "teacher_login.html")
    all_info = models.Teacher.objects.values()
    for x in all_info:
        if x["tid"] == int(uid):
            # 找到当前用户名返回页面
            msg = x["tname"]
    # 接收并处理客户修改密码
    if request.method == "POST":
        opwd = request.POST.get("opwd", None)
        npwd1 = request.POST.get("npwd1", None)
        npwd2 = request.POST.get("npwd2", None)
        if npwd1==npwd2:
            info = models.Teacher.objects.all().values("tname", "tpwd")
            for x in info:
                if x["tname"]==msg and x["tpwd"]==opwd:
                    models.Teacher.objects.filter(tname=msg).update(tpwd=npwd1)
                    change_info = "恭喜,修改密码成功!"
                if x["tname"]==msg and x["tpwd"]!=opwd:
                    error_msg = "旧密码不对哦,请再检查一下撒!"
        else:
            change_info = "两次密码不相同!"
    return render(request, 'teacher_changepwd.html',{"change_info":change_info,"error_msg":error_msg,"user_name":msg})


# 教师查询学生信息
def teacher_chechinfo(request):
    uid = request.COOKIES.get("tid")
    if not uid:
        return render(request, "teacher_login.html")
    all_info = models.Teacher.objects.values()
    for x in all_info:
        if x["tid"] == int(uid):
            # 找到当前用户名返回页面
            msg=x["tname"]
    # 查找学生的信息
    all_info = models.StudentInfo.objects.all().values()
    ulist=[]
    for x in all_info:    # x为每一个学生
        z={}
        z["sid"]=x["sid"]
        z["sname"]=x["sname"]
        z['sbirth']=x['sbirth']
        if x['ssex']:
            z['ssex']="男"
        else:
            z['ssex'] = "女"
        z['saddress']=x['saddress']
        z['sdepart']=x['sdepart']
        z['sclass']=x['sclass']
        ulist.append(z)
    return render(request, 'teacher_chechinfo.html',{"ulist":ulist,"user_name":msg})


# 通过密保找密码1
def teacher_getback_pwd(request):
    error_msg=""
    question = ""
    count=0
    if request.method == "POST":
        uname = request.POST.get("uname", None)
        all_info = models.Teacher.objects.values("tname","tphone","tquestion","tid")
        for x in all_info:
            if x["tname"]==uname:
                count+=1
                if not x["tquestion"]:
                    question = "由于您没有设置密保问题,系统默认问题为:您的电话号码?请修改密码后尽快设置密保!"
                else:
                    question = x["tquestion"]
                res=render(request,"teacher_getback_pwd2.html",{"question":question})
                res.set_cookie("mibaoid", x["tid"])
                return res
        if count==0:
            error_msg = "Sorry, 貌似么得这个账号哦,再check一下?"
    return render(request,"teacher_getback_pwd.html",{"error_msg":error_msg})

# 通过密保找密码2
def teacher_getback_pwd2(request):
    answer=""
    question=""
    msg=""
    mibaoid = request.COOKIES.get("mibaoid")
    if not mibaoid:
        return render(request, "teacher_login.html")
    if request.method == "POST":
        answer = request.POST.get("answer", None)
        all_info = models.Teacher.objects.values()
        for x in all_info:
            if x["tid"]==int(mibaoid) and x["tquestion"]=="":
                if x["tphone"]==answer:
                    msg="您的密码是:"+x["tpwd"]
                else:
                    msg="您的密保答案有误!"
                    question = "由于您没有设置密保问题,系统默认问题为:您的电话号码是?请修改密码后尽快设置密保!"
            elif x["tid"]==int(mibaoid) and x["tquestion"]!="":
                if x["tanswer"]==answer:
                    msg="您的密码是:"+x["tpwd"]
                else:
                    msg = "您的密保答案有误!"
                    question = x["tquestion"]
    return render(request,"teacher_getback_pwd2.html",{"msg":msg,"question":question})


# 设置密保问题
def teacher_setquestion(request):
    change_info = ""
    msg = ""
    uid = request.COOKIES.get("tid")
    if not uid:
        return render(request, "teacher_login.html")
    all_info = models.Teacher.objects.values()
    for x in all_info:
        if x["tid"] == int(uid):
            # 找到当前用户名返回页面
            msg = x["tname"]
    if request.method=="POST":
        question=request.POST.get("question")
        answer=request.POST.get("answer")
        answer=answer.strip()
        if not question:
            change_info="请输入密保问题"
        elif question!="" and answer!="":
            all_info = models.Teacher.objects.values()
            for x in all_info:
                if x["tid"] == int(uid):
                    models.Teacher.objects.filter(tid=x["tid"]).update(question=question,answer=answer)
                    change_info = "恭喜,密保设置成功!"
        else:
            change_info="答案不允许为空,thankss!"
    return render(request,"teacher_setquestion.html",{"user_name":msg,"change_info":change_info})


# 注册功能
def teacher_zhuce(request):
    error_msg=""
    L=[]
    all_name = models.Teacher.objects.values("tname")
    for x in all_name:
        L.append(x["tname"])
    if request.method=="POST":
        tname=request.POST.get("tname")
        tpwd1=request.POST.get("tpwd1")
        tpwd2=request.POST.get("tpwd2")
        tpost=request.POST.get("tpost")
        tphone=request.POST.get("tphone")
        tsex=request.POST.get("gender")
        tsex=int(tsex)
        if not tname:
            error_msg = "用户名不能为空"
        elif not tpwd1 or not tpwd2:
            error_msg = "密码不能为空"
        elif tpwd1!=tpwd2:
            error_msg = "两次密码不一致,请再检查"
        elif not tpost:
            error_msg = "职称不能为空"
        elif not tphone:
            error_msg = "电话号码不能为空"
        elif tname in L:
            error_msg = "sorry, 该账号已存在!"
        else:
            models.Teacher.objects.create(tname=tname,tpwd=tpwd1,tpost=tpost,tphone=tphone,tsex=tsex)
            error_msg = "恭喜,注册成功! 请返回登录"
    return render(request,"teacher_zhuce.html",{"error_msg":error_msg})





