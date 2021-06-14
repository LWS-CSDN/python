class Money:
    age=18
    name="Sz"
    
print(Money.__dict__)
# 类里面是不可以修改的,是只读的,如果想修改可以用setattr方法修改...,和geyt
# Money.__dict__={"sex":"男"}
# Money.__dict__["age"]=20
one=Money()
# one.age=18
# one.height=180
# print(one.__dict__)


#对象里是可以修改的
# one.__dict__={"name":"Sz","age":18}
# one.__dict__["age"]=999
# print(one.name)