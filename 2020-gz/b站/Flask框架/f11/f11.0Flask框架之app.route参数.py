from flask import Flask,render_template,redirect
app=Flask(__name__)

@app.route('/index',methods=['GET','POST'],redirect_to='/new')
def index():
    return "老功能"

@app.route('/new',methods=['GET','POST'])
def new():
    return "新功能"

if __name__ == '__main__':
    app.run()

'''
重定向使用场景
老页面要被淘汰,新页面还在制作
打开老页面重定向到新页面当中
后端可以做
前端也可以
-meta
-js
'''