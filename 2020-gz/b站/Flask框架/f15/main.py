'''
Flask框架之CBV和FBV

视图一般不会用CBV
一般都用FBV
'''
from flask import Flask,render_template,redirect,views

app=Flask(__name__)
import  functools
def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print('before')
        return func(*args,**kwargs)
    return inner

@app.route('/xxxx',methods=['GET','POST'])
@wapper
def index():
    return "Index"

'''
CBV
'''
class IndexView(views.View):
    methods = ['GET']
    decorators = [wapper,]

    def dispatch_request(self):
        print('Index')
        return "Index!"

app.add_url_rule('/index',view_func=IndexView.as_view(name='index'))

class IndexView(views.MethodView):
    methods=['GET']
    decorators=['GET']
    def get(self):
        return "Index.GET"
    def post(self):
        return "Index.POST"
app.add_url_rule('/index',view_func=IndexView.as_view(name='index'))


if __name__=='__main__':
    app.run()


