from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
from db.models import Teacher
from db.models import StudentInfo
from db.models import Root


def login(request):
    """用户登录"""
    # 验证用户是否登录
    if is_login(request):
        return render(request, 'root/main_Page.html')

    return render(request, 'root/login_page.html')


def logout(request):
    """用户登出"""
    if is_login(request):
        response = render(request, 'root/login_page.html')
        response.delete_cookie('username')
        return response

    return render(request, "root/login_page.html")


def main_page(request):
    """管理员主页"""

    # 获取客户端提交的用户名和密码
    form_user = request.POST.get('username')
    form_pwd = request.POST.get('password')

    root = Root.objects.all()
    if request.method == 'POST':
        for line in root:
            if line.aname == form_user and form_pwd == line.apwd:
                response = render(request, "root/main_page.html")
                # 设置cookie
                response.set_cookie('username', line.aname, 360)
                return response
        else:
            return render(request, "root/error_page.html")
    else:
        return render(request, "root/error_page.html")


def root_info_page(request):
    """管理员个人信息"""

    cookie = request.COOKIES.get('username', '')

    # 从数据库取出用户名和用户id
    context = {}
    if cookie:
        query = Root.objects.get(aname=cookie)
        if query.aname == cookie:
            username = query.aname
            uid = query.aid
            context = {"id": uid, "username": username}

    if is_login(request):
        return render(request, "root/info_page.html", context)

    return render(request, "root/error_page.html")


def teacher_manage(request):
    """教师管理"""
    # 获取所有数据对象
    all_data = Teacher.objects.all()
    # 计数器
    count = 1
    # 数据字典
    context = {}
    for line in all_data:
        #
        if line.tsex:
            sex = '男'
        else:
            sex = '女'
        # 向context(字典)追加数据(字典d)
        context.update({
            'data'+str(count): {
                'tid': str(line.tid),
                'tname': str(line.tname),
                'tpwd': str(line.tpwd),
                'tsex': sex,
                'tpost': str(line.tpost),
                'tphone': str(line.tphone),
                }
            }
        )
        count += 1

    if is_login(request):
        return render(request, "root/teacher_manage_page.html", {'context': context})

    return render(request, "root/login_page.html")


def student_manage(request):
    """学生管理"""
    all_data = StudentInfo.objects.all()
    # 计数器
    count = 1
    # 数据字典
    context = {}
    for line in all_data:
        if line.ssex:
            sex = '男'
        else:
            sex = '女'
        # 追加context(字典)
        context.update({
            'data'+str(count): {
                'sid': str(line.sid),
                'sname': line.sname,
                'spwd': line.spwd,
                'ssex': sex,
                'sbirth': line.sbirth,
                'semail': line.semail,
                'saddress': line.saddress,
                'sdepart': line.sdepart,
                'sclass': line.sclass,
                },
            }
        )
        count += 1

    if is_login(request):
        return render(request, "root/student_manage_page.html", {'context': context})
    return render(request, "root/login_page.html")


def grade_manage(request):
    """成绩管理"""
    if is_login(request):
        return render(request, "root/grade_manage_page.html")
    return render(request, "root/login_page.html")


def change_password(request):
    """修改密码"""
    if is_login(request):
        # 从数据库取出对未修改前用户密码
        old_db_pwd = Root.objects.get(aname=request.COOKIES.get("username"))
        if request.method == "POST":
            old_pwd = request.POST.get("oldPwd")
            new_pwd = request.POST.get("newPwd")
            # 验证客户端提交的旧密码和新密码是否合法
            if old_pwd != "" and new_pwd != "":
                print("提交的旧密码和新密码合法")
                if old_db_pwd.apwd == old_pwd:
                    print("旧密码与数据库原密码一致")
                    # 修改密码
                    old_db_pwd.apwd = new_pwd
                    old_db_pwd.save()
                    return render(request, "root/info_page.html", {'successful': '修改密码成功'})
                else:
                    print("旧密码与数据库原密码不一致")
                    return render(request, "root/info_page.html", {'error': '修改密码失败'})
            else:
                print("提交的旧密码和新密码不合法")
        elif request.method == "GET":
            return render(request, "root/changePwd_page.html")

        # 测试代码
        print("oldPwd:", request.POST.get("oldPwd"))
        print("oldPwd:", request.POST.get("newPwd"))
        print("更改密码后的密码:", old_db_pwd.apwd)

        return render(request, "root/info_page.html")
    return render(request, "root/error_page.html")


def change_teacher_info(request):
    """修改教师信息"""
    # 获取表单修改教师id
    fid = request.GET.get('tid')
    # 从模型获对应ID数据
    value = Teacher.objects.get(pk=int(fid))

    tsex = '男'
    if not value.tsex:
        tsex = '女'

    # 构造数据字典
    context = {
        'tid': str(value.tid),
        'tname': value.tname,
        'tpwd': value.tpwd,
        'tsex': tsex,
        'tpost': value.tpost,
        'tphone': value.tphone,
        'tquestion': value.tquestion,
        'tanswer': value.tanswer,
        'fid': fid,
    }

    if is_login(request):
        return render(request, "root/change_teacher_info_page.html", context)
    return render(request, "root/error_page.html")


def change_student_info(request):
    """修改学生信息"""
    # 控制台输出测试信息
    console_request_info(request, info="change_student_info")

    # 获取从表单提交的fid
    fid = request.GET.get('fid')

    # 获取数据库对应学生信息
    values = StudentInfo.objects.get(pk=int(fid))

    print("从DB获取的ID", values.sid)

    ssex = '男'
    if not ssex:
        ssex = '女'

    context = {
        'sid': str(values.sid),
        'sname': values.sname,
        'spwd': values.spwd,
        'sbirth': values.sbirth,
        'ssex': ssex,
        'semail': values.semail,
        'saddress': values.saddress,
        'sdepart': values.sdepart,
        'sclass': values.sclass,
    }

    # 检查用户是否已登录
    if is_login(request):
        return render(request, "root/change_student_info_page.html", context)
    return render(request, "root/error_page.html")


def save_teacher_info(request):
    """保存(修改)教师信息"""

    console_request_info(request, info="save_teacher_info")

    if is_login(request):
        return HttpResponseRedirect("teacherManage")
    return render(request, "root/error_page.html")


def is_login(cookie):
    """验证用户是否登录(cookie)"""
    username = cookie.COOKIES.get('username', '')
    if username:
        return True
    return False


def console_dict_info(info_dict):
    """控制台输出信息"""
    for key, value in info_dict.items():
        for k1, v1 in value.items():
            print(k1, ':', v1,)
        print()  # 换行


def console_teacher_info(models, fid):
    """控制台输出获取到数据模型"""
    # models 数据模型
    # fid 表单提交

    print("数据模型:", models)
    print("教师id:", models.tid)
    print("教师姓名:", models.tname)
    print("教师密码:", models.tpwd)
    print("性别:", models.tsex)
    print("职称:", models.tpost)
    print("电话:", models.tphone)
    print("密保问题:", models.tquestion)
    print("密保答案:", models.tanswer)
    print('表单提交的fid:', fid)
    print('表单数据类型:', type(fid))


def console_request_info(request, info=""):
    """控制台打印request信息"""
    print("视图方法:", info)
    if request.method == "GET":
        print("request对象:", type(request))
        values = request.GET.items()
        for k, v in values:
            print(k, ':', v)
    elif request.method == "POST":
        values = request.POST.items()
        for k, v in values:
            print(k, ":", v)
