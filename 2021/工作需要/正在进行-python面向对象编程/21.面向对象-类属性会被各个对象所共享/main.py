class Money:
    age=18
    name="sz"

one=Money()
two=Money()

print(one.age)
print(two.age)

Money.age=20
one.age=30
print(one.age)
print(two.age)