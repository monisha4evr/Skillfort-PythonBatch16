#List
a = [1,2,4,5]
a.append(6)  # [1,2,4,5,6]
a.extend([7,8]) # [1, 2, 4, 5, 6, 7, 8]
a.pop() #[1, 2, 4, 5, 6, 7] last element
a.pop(4)  # [1, 2, 4, 5, 7]  based on index
a.remove(7)  #[1, 2, 4, 5] based on items
a.reverse() #[5, 4, 2, 1]
a.sort() #[1, 2, 4, 5]
a.insert(1,9) #[1, 9, 2, 4, 5]
print(a.index(5)) # 4
print(a.count(1)) # no of occurance
print(a) #[1, 9, 2, 4, 5]
print(len(a)) #5

# tulpe 
a= (1,5,2,2,3,5,6)
print(a.index(5)) #1
print(a.count(2)) # 2

# set

a = {1,2,3,5,9,10,33} 
a.add(55) # {1, 2, 3, 33, 5, 55, 9, 10}
a.pop() # {2, 3, 33, 5, 55, 9, 10}
# a.pop(3) # no set allow to remove the items while giving the values
a.remove(2) # {3, 33, 5, 55, 9, 10}
a.update("a") # {'a', 3, 33, 5, 55, 9, 10}
print(a)

# dict
a = {
    "name" : "apple",
    "area" : "xyz",
    "phone": 9012345
}
del a ["name"] 
print(a) # {'area': 'xyz', 'phone': 9012345}

a["age"] = 20
a["age"] = 21 # update
#print(a["name"]) #KeyError: 'name' , no key as name in a
print(a.values()) 
print(a.keys())  

for key,values in a.items():
    print(key ,":", values)

print(a.get("area")) 
a.pop("area") 
print(a)

#Operator
# 1.Arithmatic
print(10 + 12)   # 22
# print(10 + "10") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10-20) # -10
print(-20 -10) # -30
print(10*2)  # 20
print('10'*2)  # 1010
print(11/2,"  |  ", 11//2)  # 5.5  |  5
print(10%5) # 0 

#2.asignment operators
c,b=10,20
print(b,c)
a=10
a+=5
print(a) # 15
a*=5
print(a) #75

#3.comparision
print(5==2) #false
print(5>=2) #True

# 4.logical  ( AND OR NOT )
a = 10
b = 20
c = 5
print(a>b and a>c) #false 
print(a>b or a>c)  #true 
print(not a)  #false

#5.Bitwise Operator
a = 1      # 0001
b= 2       # 0010
print(a&b) # 0
print(a|b) # 3
print(~a)  # -2 -(n+1)
print(a>>2) #0001 >> 00 + 0000   ans : 0
print(a<<2) # 0001 << 00 + 0100  ans : 4

#6.membership operator (in ,not in)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a 

print(2 in list_a) #True
print(5 in list_a) #false
print(5 not in list_a)#true


#7.Identity Operator (is,isnot)
print(list_a is list_b) #false
print(list_a is list_c) #true
print(list_a is not list_c) #true