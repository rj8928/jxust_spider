# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BukaoTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('busername', models.CharField(max_length=30)),
                ('bclassname', models.CharField(max_length=40)),
                ('bcoursename', models.CharField(max_length=40)),
                ('bxuefen', models.CharField(max_length=5)),
                ('bcoursekind', models.CharField(max_length=15)),
                ('bteacher', models.CharField(max_length=20)),
                ('bxueyuan', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'BukaoTable',
            },
        ),
        migrations.CreateModel(
            name='CourseMark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xuenian', models.CharField(max_length=15)),
                ('xueqi', models.CharField(max_length=5)),
                ('kechengdaima', models.CharField(max_length=15)),
                ('kechengmingcheng', models.CharField(max_length=20)),
                ('kechengxinzhi', models.CharField(max_length=20)),
                ('xuefen', models.CharField(max_length=5)),
                ('jidian', models.CharField(max_length=5)),
                ('chengji', models.IntegerField(db_index=True)),
                ('fuxiubiaoji', models.BooleanField(default=False)),
                ('bukaochengji', models.IntegerField(null=True)),
                ('chongxiuchengji', models.IntegerField(null=True)),
                ('xueyuanmingcheng', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'CourseMark',
            },
        ),
        migrations.CreateModel(
            name='CourseTableInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'CourseTable',
            },
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('suserid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('sxueyuan', models.CharField(max_length=30)),
                ('snianji', models.CharField(max_length=5)),
                ('szhuanye', models.CharField(max_length=40)),
                ('sclassname', models.CharField(max_length=40)),
                ('susername', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'StudentList',
            },
        ),
        migrations.CreateModel(
            name='SumCourseTable',
            fields=[
                ('coursetable', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('zhuanyename', models.CharField(max_length=40)),
                ('xuenian', models.CharField(max_length=15)),
                ('banjiname', models.CharField(max_length=40)),
                ('nianji', models.CharField(max_length=5)),
                ('xueqi', models.CharField(max_length=3)),
                ('xueyuanname', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'SumCourseTable',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uuserid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('upwssword', models.CharField(max_length=40)),
                ('uusername', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='coursetableinfo',
            name='coursetable',
            field=models.ForeignKey(to='chengji.SumCourseTable'),
        ),
        migrations.AddField(
            model_name='coursemark',
            name='userid',
            field=models.ForeignKey(to='chengji.UserInfo'),
        ),
        migrations.AddField(
            model_name='bukaotable',
            name='buserid',
            field=models.ForeignKey(to='chengji.StudentList'),
        ),
    ]
