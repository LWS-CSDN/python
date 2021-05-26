class Person:
    pass

p=Person()

p.pets=["小花","小黑"]
print(p.pets,id(p.pets))

#内存地址没有变
#p.pets这是先取来,再用方法,所以不改变内存地址
p.pets.append("小黄")
print(p.pets,id(p.pets))

#说明了重新开辟了一块内存空间
#这个是先取出来,然后重新赋值,开辟新的内存空间
p.pets=[1,2]
print(p.pets,id(p.pets))
