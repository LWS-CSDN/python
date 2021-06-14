class Person:
    def eat(self,food):
        print("在吃饭",food)

# p=Person()
# print(p)
# p.eat("土豆")

print(Person.eat)
Person(123,"abc")

func=Person.eat
func("abc",999)