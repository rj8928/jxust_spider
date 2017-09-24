# coding=utf-8
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    uuserid = models.CharField(max_length= 15, primary_key=True)
    upwssword = models.CharField(max_length=40)
    uusername = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.uuserid

    class Meta:
        db_table = 'UserInfo'


class CourseMark(models.Model):
    userid = models.ForeignKey(UserInfo)
    xuenian = models.CharField(max_length=15)
    xueqi = models.CharField(max_length=5)
    kechengdaima = models.CharField(max_length=15)
    kechengmingcheng = models.CharField(max_length=20)
    kechengxinzhi = models.CharField(max_length=20)
    xuefen = models.CharField(max_length=5)
    jidian = models.CharField(max_length=5)
    chengji = models.IntegerField(db_index=True)
    fuxiubiaoji = models.BooleanField(default=False)
    bukaochengji = models.IntegerField(null=True)
    chongxiuchengji = models.IntegerField(null=True)
    xueyuanmingcheng = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.kechengmingcheng

    def cxuenian(self):
        return self.xuenian
    xuenian.short_description = '学年'
    def cxueqi(self):
        return self.xuenian
    xuenian.short_description = '学期'
    def ckechengdaima(self):
        return self.xuenian
    xuenian.short_description = '课程代码'
    def ckechengmingcheng(self):
        return self.xuenian
    xuenian.short_description = '课程名称'
    def ckechengxinzhi(self):
        return self.xuenian
    xuenian.short_description = '课程性质'
    def cxuefen(self):
        return self.xuenian
    xuenian.short_description = '学分'
    def cjidian(self):
        return self.xuenian
    xuenian.short_description = '绩点'
    def cchengji(self):
        return self.xuenian
    xuenian.short_description = '成绩'
    def cfuxiubiaoji(self):
        return self.xuenian
    xuenian.short_description = '辅修标记'
    def cbukaochengji(self):
        return self.xuenian
    xuenian.short_description = '补考成绩'
    def cchongxiuchengji(self):
        return self.xuenian
    xuenian.short_description = '重修成绩'
    def cxueyuanmingcheng(self):
        return self.xuenian
    xuenian.short_description = '学院名称'


    class Meta:
        db_table = 'CourseMark'


class StudentList(models.Model):
    suserid = models.CharField(max_length=15, primary_key=True)
    sxueyuan = models.CharField(max_length=30)
    snianji = models.CharField(max_length=5)
    szhuanye = models.CharField(max_length=40)
    sclassname = models.CharField(max_length=40)
    susername = models.CharField(max_length=30)

    class Meta:
        db_table = 'StudentList'


class  SumCourseTable(models.Model):
    coursetable = models.CharField(max_length=30,primary_key=True)
    zhuanyename = models.CharField(max_length=40)
    xuenian = models.CharField(max_length=15)
    banjiname = models.CharField(max_length=40)
    nianji = models.CharField(max_length=5)
    xueqi = models.CharField(max_length=3)
    xueyuanname= models.CharField(max_length=40)

    class Meta:
        db_table = 'SumCourseTable'


class CourseTableInfo(models.Model):
    coursetable = models.ForeignKey(SumCourseTable)
    teacher = models.CharField(max_length=15)
    course = models.CharField(max_length=40)

    class Meta:
        db_table = 'CourseTable'


class BukaoTable(models.Model):
    buserid = models.ForeignKey(StudentList)
    busername = models.CharField(max_length=30)
    bclassname = models.CharField(max_length=40)
    bcoursename= models.CharField(max_length=40)
    bxuefen = models.CharField(max_length=5)
    bcoursekind = models.CharField(max_length=15)
    bteacher = models.CharField(max_length=20)
    bxueyuan = models.CharField(max_length=30)

    class Meta:
        db_table = 'BukaoTable'






