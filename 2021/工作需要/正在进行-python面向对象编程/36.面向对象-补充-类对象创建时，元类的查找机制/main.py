class Animal:
    pass
class Person:
    __metaclass__=xxx
    pass

# 1.检测对象中是否有明确__metaclass__属性

# 2.检测父类中是否存在__metaclass__属性
# 3.检测模块是否存在__metaclass__属性
# 4.通过内置的type这个元类,来创建这个类对象

# 元类的应用场景
# 1.拦截类的创建
# 2.修改类
# 3.返回修改之后的类
