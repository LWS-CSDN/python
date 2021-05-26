from flask import Flask,Response
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route('/index')
#application/json
def index():
    return {
        'a':'北京',
        'b':'上海',
        'c':'深圳'
    }

@app.route('/index1')
#Content-Type:text/html; charset=utf-8
def index1():
    return '<h1>北京</h1>'

@app.route('/index2')
def index2():
    return ('bejing','shanghai','shenzhen')

@app.route('/index3')
def index3():
    return Response('大家想好')

if __name__ == '__main__':
    app.run()