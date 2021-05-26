from flask import Flask, make_response,Response

app = Flask(__name__)

@app.route('/index2')
def index2():
    s='''
    <title>服务器内部错误</title>
    <h1>Not Found</h1>
    <p></p>
    '''
    return s,500

@app.route('index3')
def index3():
    response=Response('<h1>中午吃什么</h1>')
    print(response.content_type)
    print(response.headers)
    print(response.status_code)
    print(response.status)
    response.set_cookie('name','翔宇')
    return response

@app.route('/index4')
def index4():
    content='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
欢迎来到购物网站
</body>
</html>'''
    response=make_response(content)
    response.headers['mytest']='123abc'
    response.headers['myhello']='hello'
    return  response

if __name__ == '__main__':
    app.run()
