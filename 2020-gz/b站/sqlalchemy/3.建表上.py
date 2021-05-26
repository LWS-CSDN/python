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

db=SQLAlchemy(app)

#学生表
class Student(db.Model):
    __tablename__="student"
    #主键
    id=
    name=
    gender=
    phone=

#课程表
class Course(db.Model):
    __tablename__="course"
    id=
    name=
    teacher=

#教师表
class Teacher(db.Model):
    __tablename__="teacher"
    id=
    name=
    gender=
    phone=

#成绩表
class Grade(db.Model):
    __tablename__="grade"
    id=
    course_name=
    grade=
    student=
