"""
私有属性的实现机制
-名字重整
重改__x为另外一个名称,如_类名__x
-目的
防止外界直接访问
防止被子类同名称属性覆盖
尽量不要使用
"""
class Animal:
    __x=10

a=Animal()
print(Animal.__dict__)
print(Animal._Animal__x)