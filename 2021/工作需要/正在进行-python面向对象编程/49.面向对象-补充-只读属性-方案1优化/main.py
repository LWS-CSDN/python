class Person(object):
    def __init__(self):
        self.__age=18
    
    #主要作用就是,可以以使用属性的方式,来使用这个方法
    @property
    def age(self):
        return self.__age

p1=Person()
print(p1.age)


#p1.age=666