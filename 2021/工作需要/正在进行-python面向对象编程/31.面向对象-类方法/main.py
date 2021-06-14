class Person:
    @classmethod
    def aaa(cls,a):
        print("这是一个类方法",cls,a)

Person.aaa(123)

p=Person()
p.aaa(666)


func=Person.aaa
func(111)

class A(Person):
    pass

A.aaa(0)