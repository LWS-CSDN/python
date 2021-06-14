num=10
def run(self):
    print("---",self)
xxx=type("Dog",(),{"count":0,"run":run})
print(xxx)
print(xxx.run())
print(xxx.__dict__)

d=xxx()
print(d)
d.run()