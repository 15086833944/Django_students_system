from django.urls import path
from . import views


urlpatterns = [
    path('', views.teacher_login),
    path('teacher_login', views.teacher_login),
    path('teacher_self_info', views.teacher_self_info),
    path('teacher_changepwd', views.teacher_changepwd),
    path('teacher_chechinfo', views.teacher_chechinfo),
    path('teacher_getback_pwd', views.teacher_getback_pwd),
    path('teacher_getback_pwd2', views.teacher_getback_pwd2),
    path('teacher_setquestion', views.teacher_setquestion),
    path('teacher_zhuce', views.teacher_zhuce),

]
