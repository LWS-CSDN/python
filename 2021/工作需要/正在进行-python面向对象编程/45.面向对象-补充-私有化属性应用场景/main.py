"""
应用场景
数据保护
数据过滤
"""
class Person:
    def __init__(self):
        self.__age=18
    def setAge(self,value):
        if isinstance(value,int) and 0<value<200:
            self.__age=value
        else:
            print("您输入的数据有问题,请重新输入")
        
    def getAge(self):
        return self.__age
p1=Person()
# p2=Person()
p1.age=-10
# print(p1.age)
# print(p2.age)

print(p1.__dict__)
print(p1.setAge("abc"))