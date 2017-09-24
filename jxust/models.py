# coding=utf-8
from django.db import models

# Create your models here.
class CourseMark(models.Model):
    userid = models.CharField(max_length=10)
    xuenian = models.CharField(max_length=15)
    xueqi = models.IntegerField()
    kechengdaima = models.CharField(max_length=10)
    kechengmingcheng = models.CharField(max_length=20)
    kechengxinzhi = models.CharField(max_length=10)
    xuefen = models.DecimalField(max_digits=2,decimal_places=1)
    jidian = models.DecimalField(max_digits=3, decimal_places=2)
    chengji = models.IntegerField()
    fuxiubiaoji = models.BooleanField(default=False)
    bukaochengji = models.IntegerField(null=True)
    chongxiuchengji = models.IntegerField(null=True)
    xueyuanmingcheng = models.CharField(max_length=15,null=True)
    teacher = models.CharField(max_length=20, null=True)
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
    def cteacher(self):
        return self.xuenian
    xuenian.short_description = '老师'


class UserInfo(models.Model):
    userid = models.IntegerField(primary_key=True)
    pwssword = models.CharField(max_length=40)

    def __str__(self):
        return self.userid