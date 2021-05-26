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

#增
s1=Student(name="张三",gender="男",phone="")
#s2=Student(name="张三",gender="男",phone="")

#语句 第一种
# db.session.add(s1)
# db.session.commit()

# db.session.add_all([s1,s2,s3,s4])
# db.session.commit()

#查
#get
# stu=Student.query.get(1)
# print(stu.name)
# print(stu.gender)
# print(stu.phone)

#all()查全部
# stu=Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

#filter() 条件查询
# stu=Student.query.filter(Student.id>=5)
# for i in stu:
#     print(i.name,i.id)

#filter_by() 比较类似SQL的查询 first()
# stu=Student.query.filter_by(name="张三").all()
# stu=Student.query.filter_by(name="张三").first()
stu=Student.query.filter_by(name="张三").filter(Student.id==2)

for i in stu:
    print(i.name,i.id)




#改
stu=Student.query.get(1)
    ``
#删