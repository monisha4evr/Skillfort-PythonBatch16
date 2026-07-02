print(int("abc"))
print(int("123"))

a=10
b=20
a,b=b,a
print(a,b)

print(0 or 20)


a=[1,2,3]
b=[1,2,3]
c=b
d=b.copy()
c.append(5)
d.append(6)
print(b)


a=[1,2,3]
b=[1,2,3]
print(a is b)


a=10
b=10
print(a is b)

a=["apple"]*3
print(a)

a=["apple"]+3
print(a)

a="flowers"
print(a[::-1])

a="i am Learning Python"
a =["i","am","Nagaraj"]
print(" ".join(a))


names = ["Ram", "Sam"]
marks = [80, 90]

for name, mark in zip(names, marks):
    print(name, mark)



names = ["Ram", "Sam"]
marks = [80, 90]    
print(list(zip(names, marks))) 


class Agelimit(Exception):
    pass 

def check_age(age) :
    if age<18:
        raise Agelimit("Age is Lesser than 18")
    
try :
    check_age(13)
except Agelimit as e:
    print(e)

    

class Test:
    def __init__(self,name,numb,pwd):
        self.name=name
        self._numb=numb
        self.__pwd=pwd

    def get_password(self):
        print(self.__pwd)

t=Test("Isai",123,"@123")
print(t.name)
print(t._numb)
print(t._Test__pwd)
t.get_password()


