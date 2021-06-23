class Animal:
    x=10
    def test(self):
        print(Animal.x)
        print(self.x)

class Dog(Animal):
    def test2(self):
        print(Dog.x)
        print(self.x)
    

#测试代码
# a=Animal()
# a.test()

# d=Dog()
# d.test2()
a=666