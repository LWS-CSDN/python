class Person(object):
    def __init__(self):
        self.__age=18
    
    def get_age(self):
        print("----,get")
        return self.__age

    def set_age(self,value):
        print("----,set")
        self.__age=value
    
    age=property(get_age,set_age)

p=Person()
print(p.age)

p.age=90
print(p.age)
print(p.__dict__)

#第二种使用方式
class Person2(object):
    def __init__(self):
        self.__age=18
    
    @property
    def age(self):
        print("----,get")
        return self.__age
    
    @age.setter
    def age(self,value):
        print("----,set")
        self.__age=value
    
p=Person2()
print(p.age)

p.age=10
print(p.age)
        