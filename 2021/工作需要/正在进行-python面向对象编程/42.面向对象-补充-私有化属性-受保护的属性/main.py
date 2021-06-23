class Animal:
    _x=10
    def test(self):
        print(Animal._x)
        print(self._x)

class Dog(Animal):
    def test2(self):
        print(Dog._x)
        print(self._x)
    

#测试代码
# a=Animal()
# a.test()

# d=Dog()
# d.test2()
__all__=["_a"]
_a=666