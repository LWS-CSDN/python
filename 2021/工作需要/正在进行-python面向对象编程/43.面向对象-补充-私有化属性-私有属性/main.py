class Animal:
    __x=10
    def test(self):
        print(Animal.__x)
        print(self.__x)

class Dog(Animal):
    def test2(self):
        """
        访问不了
        """
        print(Dog.__x)
        print(self.__x)


# a=Animal()
# a.test()


#访问不了私有属性
# print(Animal.__x)
# print(a.__x)


# d=Dog()
# d.test2()
__all__=["__a"]
__a=666