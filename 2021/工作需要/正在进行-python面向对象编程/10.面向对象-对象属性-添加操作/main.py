#1.定义一个类
class Person:
    pass

#2.根据类,创建一个对象
p=Person()
#3.给p对象，增加一些属性
p.age=18
p.height=180
#4.验证是否有添加成功
# print(p.age)
print(p.__dict__)