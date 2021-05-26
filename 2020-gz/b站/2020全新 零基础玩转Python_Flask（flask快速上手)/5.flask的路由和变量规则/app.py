from flask import Flask
import settings
app = Flask(__name__)
app.config.from_object(settings)

data={'a':'北京','b':'上海','c':'深圳'}

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getcity/<key>')
#key就是一个变量名,默认是字符串类型的
def get_city(key):
    print(key)
    print(type(key))
    return data.get(key)

@app.route('/add/<int:num>')
def add(num):
    result=num+10
    return str(result)

# def index():
#     return "welcome everyone"
#
# app.add_url_rule("/index",view_func=index)


if __name__ == '__main__':
    app.run()
