# 1.variables (Like Container)
# ------------
#Naming Rules
# a1
# _adf
# first_name
# (a-z) (A-Z) (0-9)
# reserved keyword - if for 

2. data types
1.numbers (int whole , float -decimal )
2 sequenced (string(str), list,tuple,range)
3 set and map (set, dictionary(dict))
4.bool, None


# immutable
int,str,float,bool,tuple
a=10
print(a)
print(id(a)) # to check Address
a=5
print(a)
print(id(a))

#mutable
list,set,dict
#eg:
a=[1,2,3]
print(a)
print(id(a))
a[2]=7
print(a)
print(id(a))

#type conversion
1. Implicit (Automatic)
2. Explicit (manual)

#type()
a=10
print(type(a))
a="abc"
print(type(a))
a=0.0
print(type(a))
a=[1,2,3]
print(type(a))
a=(1,2,3)
print(type(a))

a=10
b=10.5
c=a+b # implicit example
print(type(c))

a=int("123")
b=123
c=a+b
print("a=",type(a),"b=",type(b))
print(c,type(c))

a="123"
b=str(123)
c=a+b
print("a=",type(a),"b=",type(b))
print(c,type(c))

a=int("abc")
b=123
c=a+b
print("a=",type(a),"b=",type(b))
print(c,type(c))

a="abc"
b=str(123)  # explicit
c=a+b
print("a=",type(a),"b=",type(b))
print(c,type(c))

# operators:
# 1. Arithmetic
# 2. Asignment
# 3. comparision
# 4. Logical
# 5. Bitwise
# 6. Membership
# 7. Identity

# 1.Arithmetic Operator (+,-,*,/,//,**)
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%2)
print(a**3)

# 2. Asignment
d=10
a,b,c=15,20,30
print(a)
a+=10 #(a=a+10)
print(a)

# 3.comparision
a=10
b=20
print(a == b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

# 4.logical
and , or , not
and

True true =>True
true false => false
false true => false
false false => false

or 
true true => true
false true => true
true false => true
false false => false

not 
true -> False
false -> True

a=10
b=20
c=30
print(a>b and a>c) # false
print(a<b and a>c) #false
print(a<b and a<c) #True

print(a>b or a>c) #false
print(a<b or a>c) #True
print(a<b or a<c) #True
a=10
print (not bool(a)) #false

a=0
print (not bool(a)) #false

# Truthy falsy
#Falsy
0,0.0,'',{},[],

print(0 and 10)


# bitwise (binary )
a=10 #=> 1010
b=5  #=> 0101
#and     0000
#or      1111
print(a&b)
print(a|b)
print(~a) #-(n+1)  -11
#>>
a=10 #=> 1010
print(a>>2) #0010 10
#<<
a=8 # 100000 => 32
print(a<<2)
a=5 # 010100  => 20
print(a<<2)

membership

a=[1,2,3,4]
print( 2 in a)
print( 2 not in a)

# identity
#     is , is not
    
a=10
b=10
print(id(a),id(b))
print(a is b)

a=[1,2,3]
b=[1,2,3,4]
print(id(a),id(b))
print(a is b)
print( a is not b)

# collection:
# ------------
1. list
2. tuple
3. set
4. dict

# 1. list
#     collection of hetrogenous data 
#     denoted by  []
#     1.ordered
#     2.mutable
#     3.allow duplicate
#     eg: [1,2,6,3,9,2]
a=[1,2,3]
a.append(9)
print(a)
a.pop()
print(a)
a.clear()
print(a)
    
# 2. tuple
#     collection of hetrogenous data 
#     denoted by ()
#     1.ordered
#     2.immutable
#     3.allow duplicate
#     eg: (1,6,1,3,4)

a=(1,2,3,2)
print(a.count(3)) #1
print(a.index(2)) #1 -> first occurance position
# print(a.index(8)) Error
    
# 3. set
#     collection of hetrogenous data 
#     denoted by {}
#     1.unordered
#     2.not allow duplicates
#     3.mutable
    
#     eg: {1,3,4,6}

a={1,2}
a.add(3)
print(a)
c=a
print(c)
c.add(4)
print(c)
b=a.copy()
print(b)
a.clear()
print(a)

a.union(b)
    
# 4. dict
#     collection of hetrogenous data
#     denoted by { key:value }
#     1.ordered
#     2.key is unique , value accept duplicate
#     3.mutable
#     eg: {"name":"apple","color":"red","stock":50,"price":66.9}

a={"name":"apple","color":"red","stock":50,"price":66.9}
a['city']="kashmir"
a['price']=100
for i in a.keys():
    print(i)
    
for i in a.values():
    print(i)
    
for k,v in a.items():
    print("k=>",k,"values=>",v)

a={1,2,3}
b=a
print(a,b)
print(id(a),id(b))
c=a.copy()
print(a,b,c)
print(id(a),id(b),id(c))
c.add(4)
print(f"output a={a},  b={b} ,  c={c}")






    