#Logical

print(10 and 0)
print(0 and 10)
print(10 and 1)
print(10 or 0)
print(0 or 10)
print(15 or 10)

membership
#in not
a=[1,2,3,4]
print(2 not in a)

identity
is, is not

a=10
b=10
print(id(a),id(b))

print(a is b)

a=[10,20,30]
b=[10,20,30]
print(id(a),id(b))
print(a is b)

a=(10,20,30)
b=(10,20,30)
print(id(a),id(b))
print(a is b)


print("Truth" if -1 else "False")

a=[]
b=()
c={1,2}
d={"k":"v"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a=(1,)
print(type(a))

a="123"
b=str(123)
print(a+b)

print("*"*3)
a=[1,2,3]
print(a+[3])


a={1,2,3}
b={1,2,3}
c=b
d=b.copy()
c.add(4)
print(a,b,c,d)