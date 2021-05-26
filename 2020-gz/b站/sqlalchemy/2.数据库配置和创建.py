from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app=Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+"/home/lmp/test.db"

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@127.0.0.1:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="jjjsks"

db=SQLAlchemy(app)


