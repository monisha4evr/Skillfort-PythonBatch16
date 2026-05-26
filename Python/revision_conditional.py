# ternary operator (or) Conditional Expression
# truthy Falsy
# Slicing
# logical operator and
# Bitwise (not)  and Shift
# Chained Boolean Logic "A" or "B" and "c" 
# Loop 
# Conditional Statement 
# member operator in tuple , list + tuple (1,2,3,[1,2])
# identity check

# Ternary operator
a=12
if a%2==0:
    print("Even")
else:
    print("odd")
    

a="welcome to python class"
#print(a[11])
#print(a[1:2])
#print(a[1:])
#print(a[:5])
#print(a[::-1])

# bitwise and

a=12
print(~a)

a=3 #=>  0011
b=2 #=>  0010
# a&b=>  0010
print(a&b)

a=2  0000       10
print(a>>2)

Task 1
s=90-100
a=80-89
b=60-79
c=below 60

Task 2
item=[0,0.0," ",(),{},None]
print([bool(i) for i in item])

a=-1
if -1:
    print("true")
else :
    print("False")

a=(1,2,3,[4,5])
print(a[3])
a[3]+=[7,8]
print(a)

a=[1,2]
print(a+1)

