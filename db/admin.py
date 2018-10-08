from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Root)
class RootAdmin(admin.ModelAdmin):
    list_display = ('aid', 'aname', 'apwd')


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('sid', 'sname', 'sbirth', 'ssex', 'semail', 'saddress', 'sdepart', 'sclass')


@admin.register(ClassTable)
class ClassTableAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname', 'chour', 'ctime')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('sid', 'cid', 'score', 'stime')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('classid', 'cname')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('tid', 'tname', 'tpost', 'tsex', 'tphone')
