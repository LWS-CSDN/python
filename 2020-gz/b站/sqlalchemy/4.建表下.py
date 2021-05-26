'''
班级

学生表
-id
-name
-sex
-phone
课程表
-id
-name
-teacher
教师表
-id
-name
-gender
-phone
成绩表
-id
-course_name
-grade(分数)
-student
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app=Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+"/home/lmp/test.db"

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@127.0.0.1:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="jjjsks"

db=SQLAlchemy(app)#实例化数据库

#学生表
class Student(db.Model):
    __tablename__="student"
    id=db.Column(db.Integer,primary_key=True)#主键
    name=db.Column(db.String(64),nullable=False)#学生名字 nullable能否为空
    gender=db.Column(db.Enum("男","女"),nullable=False)#性别 Enum枚举 不能为空
    phone=db.Column(db.String(11))#手机号 可以为空

#课程表
class Course(db.Model):
    __tablename__="course"
    id=db.Column(db.Integer,primary_key=True)#主键
    name=db.Column(db.String(64),nullable=False)#课名
   

#教师表
class Teacher(db.Model):
    __tablename__="teacher"
    id=db.Column(db.Integer,primary_key=True)#主键
    name=db.Column(db.String(64),nullable=False)
    gender=db.Column(db.Enum("男","女"),nullable=False)
    phone=db.Column(db.String(11))

#成绩表
# class Grade(db.Model):
#     __tablename__="grade"
#     id=
#     course_id=
#     grade=
#     student=
if __name__=="__main__":
    db.create_all()
