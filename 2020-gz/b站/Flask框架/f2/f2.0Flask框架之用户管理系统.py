from flask import Flask,render_template,request,redirect,session

#默认是templates
app=Flask(__name__)#一个Flask类的对象
app.secret_key='asdfasfasfASFARFWE4'
#也可以修改成其他的
#app=Flask(__name__,template_folder='')


@app.route('/login',methods=['GET','POST'])
def login():
    print("请求来了")
    if request.method=='GET':
        return render_template('login.html')
    user=request.form.get('user')#获取POST传过来的值
    pwd=request.form.get('pwd')#获取POST传过来的值
    if user=='alex' and pwd=='123':
        #用户信息放入session
        session['user_info']=user
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误')
        #return render_template('login.html',**{'msg':'用户名或密码错误'})
@app.route('/index')
def index():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    return "欢迎登陆"

@app.route('/logout')
def logout():
    '''
    注销
    '''
    del session["user_info"]
    return redirect('/login')
if __name__ == '__main__':
    app.run() #run_simple(host,port,app)
