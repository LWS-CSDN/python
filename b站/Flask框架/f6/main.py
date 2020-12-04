'''
内容回顾:
1.装饰器
问题:什么是装饰器?
问题:手写装饰器
问题:装饰器都在哪里用过

def xx(x):
    def oo(xx):
        #执行原来的代码

def xx(x):
    @functools.wraps(oo)
    def oo(xx):
        #执行原来的代码
        return

def xx(func):
    def oo(*args,**kwargs):
        #执行原来的代码
        return func(*args,**kwargs)
    return oo

今日内容:
1.配置文件
2.路由*
3.视图函数
4.请求和响应*
5.模板
6.session*
7.闪现
8.蓝图 blueprint*
9.常见装饰器*
10.中间件
11.
'''