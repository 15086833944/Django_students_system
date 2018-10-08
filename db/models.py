from django.db import models

# Create your models here.


class Root(models.Model):
    """管理员表"""
    aid = models.AutoField(primary_key=True)  # 管理员ID
    aname = models.CharField(max_length=30)  # 管理员用户名
    apwd = models.CharField(max_length=15)  # 管理员密码


class StudentInfo(models.Model):
    """学生信息表"""
    sid = models.AutoField(primary_key=True)  # 学号
    sname = models.CharField(max_length=20)  # 姓名
    spwd = models.CharField(max_length=15)  # 密码
    sbirth = models.DateTimeField()  # 生日
    ssex = models.BooleanField(default=False)  # 性别
    semail = models.EmailField(max_length=100)  # email
    saddress = models.CharField(max_length=100)  # 地址
    sdepart = models.CharField(max_length=30)  # 系别/电话
    sclass = models.CharField(max_length=30)  # 班级


class Teacher(models.Model):
    """教师信息表"""
    tid = models.AutoField(primary_key=True)  # 教师id
    tname = models.CharField(max_length=20)  # 教师姓名
    tpwd = models.CharField(max_length=15)  # 密码
    tsex = models.BooleanField(default=True)  # 性别
    tpost = models.CharField(max_length=30)  # 职称
    tphone = models.CharField(max_length=20)  # 联系方式
    tquestion = models.CharField(max_length=50, default='')  # 密保
    tanswer = models.CharField(max_length=50, default='')  # 密保答案


class ClassTable(models.Model):
    """课程表"""
    cid = models.AutoField(primary_key=True)  # 课程编号
    cname = models.CharField(max_length=30)  # 课程名称
    chour = models.IntegerField(default=0)  # 课时
    ctime = models.DateTimeField()  # 日期时间


class Grade(models.Model):
    """成绩表"""
    sid = models.AutoField(primary_key=True)  # 学生id(关联外键)
    cid = models.IntegerField()  # 课程表ID(关联外键)
    score = models.IntegerField(default=0)  # 分数
    score0 = models.IntegerField(default=0)  # 分数
    score1 = models.IntegerField(default=0)  # 分数
    score2 = models.IntegerField(default=0)  # 分数
    score3 = models.IntegerField(default=0)  # 分数
    score4 = models.IntegerField(default=0)  # 分数
    score5 = models.IntegerField(default=0)  # 分数
    stime = models.DateTimeField()  # 日期时间


class Class(models.Model):
    """班级表"""
    classid = models.AutoField(primary_key=True)  # 班级表
    cname = models.CharField(max_length=30)  # 班级名称

