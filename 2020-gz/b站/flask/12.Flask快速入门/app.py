from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/login')
def hello_world2():
    name=request.values.get("name")
    pwd=request.values.get("pwd")
    return f'name={name},pwd={pwd}'

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/tem')
def hello_world3():
    return render_template('index.html')

@app.route('/abc')
def hello_world1():
    id=request.values.get("id")
    print(id)
    return f"""
    <form action="/login">
        账号:<input name="name" value="{id}"><br/>
        密码:<input name="pwd" type="password">
        <input type="submit">
    </form>
    """

if __name__=='__main__':
    app.run()