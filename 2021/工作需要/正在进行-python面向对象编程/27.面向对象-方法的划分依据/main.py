# 方法的划分
# 1.实例方法
# 默认第一个参数需要接收到一个实例
# 2.类方法
# 默认第一个参数需要接收到一个类
# 3.静态方法
# 静静的看着前面俩装b,第一个参数啥也不默认接收
class Person:
    def eat(self):
        print("这是一个实例方法",self)

    @classmethod
    def aaa(cls):
        print("这是一个类方法",cls)

    @staticmethod
    def bbb():
        print("这是一个静态方法")

# p=Person()
# print(p)
# p.eat()

#Person.aaa()

#Person.bbb()