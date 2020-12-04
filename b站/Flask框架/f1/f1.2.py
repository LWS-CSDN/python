from flask import Flask

app=Flask(__name__)#一个Flask类的对象

@app.route('/index')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run() #run_simple(host,port,app)
