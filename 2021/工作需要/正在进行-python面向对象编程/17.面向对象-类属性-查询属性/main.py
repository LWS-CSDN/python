class Test:
    sex='男'
class Money:
    age=18
    count=1
    num=0

one=Money()
one.sex='女'
one.__class__=Test
print(one.__class__)

print(one.sex)
# print(one.age)
# print(one.count)

'''
为什么可以通过对象访问到类属性?
答:和python对象的属性查找机制有关
1.优先到对象自身(one)去查找属性  找到则结束
2.如果没有找到则根据_class_找到对象对应的类(Money),
到这个类里面查找
'''