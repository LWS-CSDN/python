"""
经典类没有继承object
python2.x如果定义一个类,没有显示的继承object,那么这个类就是一个经典类
必须显示的继承自,object,它才是一个新式类

新式类继承object
python3.x,如果直接定义一个类,会隐式的继承object,默认情况下,就已经是一个新式类

"""
#python2.x版本运行
class Person:
    pass
print(Person.__bases__)#()


class Person1(object):
    pass
print(Person1.__bases__)#(<class 'object'>,)




#python3.x版本运行
class Person2:
    pass
print(Person2.__bases__)#(<class 'object'>,)

class Person3(object):
    pass
print(Person3.__bases__)#(<class 'object'>,)


