from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('logout', views.logout),
    path('mainPage', views.main_page),
    path('infoPage', views.root_info_page),
    path('studentManage', views.student_manage),
    path('teacherManage', views.teacher_manage),
    path('gradeManage', views.grade_manage),
    path('changePwd', views.change_password),
    path('changeTeacherInfo', views.change_teacher_info),
    path('changeStudentInfo', views.change_student_info),
    path('saveTeacherInfo', views.save_teacher_info),
]
