num=10
print(num.__class__)

s="abc"
print(s.__class__)

class Person:
    pass
p=Person()
print(p.__class__)

print("-"*10)

print(num.__class__.__class__)
print(int.__class__)
print(str.__class__)
print(Person.__class__)
print(type.__class__)
#type(元类)