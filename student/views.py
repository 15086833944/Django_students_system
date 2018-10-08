from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from db.models import StudentInfo
from db.models import Grade
# 学生APP视图


def login(request):
    """用户登录"""

    # 测试代码,检查是否提交用户名和密码是否提交到后台 start
    print(request.GET.get('username'))
    print(request.GET.get('password'))

    # info = StudentInfo.objects.get(sname=request.GET.get('username'))
    # print("从数据库获取到的信息", info.sname)

    return render(request, "student/student_login.html")


def logout(request):
    """用户注销"""
    return HttpResponse('学生退出')


def main_page(request):
    """业务处理"""

    # 测试 是否成功获取客户端提交的表单数据
    print(request.POST.get('uname'))
    print(request.POST.get('mima'))

    try:
        in_name = int(request.POST.get('uname'))
        in_pwd = request.POST.get('mima')

        uid = StudentInfo.objects.get(pk=in_name)
        gid = Grade.objects.get(pk=uid.sid)
        upwd = uid.spwd

        if (in_name == uid.sid) and (in_pwd == upwd):
            print("用户名匹配成功")
            return render(request, "student/student_page.html", {'uid': uid, 'gid': gid})
    except Exception as e:
        print("匹配失败", e)

    return HttpResponse("用户名不正确或密码不正确 <a href='login'>登录</>")


