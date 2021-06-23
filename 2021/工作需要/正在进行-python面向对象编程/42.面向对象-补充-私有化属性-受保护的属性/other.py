# import main

# print(main._a)

from main import *
"""
有__all__指明对应变量才可以访问
没有__all__指明对应变量不可以访问,报错
"""
print(_a)