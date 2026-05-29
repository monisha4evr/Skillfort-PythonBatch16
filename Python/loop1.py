for i in range(1,6):
    print(i)
    
a=list(range(6))
print(a)

n=3
for i in range(0,n):
    for j in range(0,n):
        print("(",i,j,")",end=" ")
       # print(f"({i}{j})",end=" ")
    print()
    
# i=0
#     j=0  #(0,0) 
#     j=1  #(0,1) 
#     j=2  #(0,2)
#     j=3 -
# i=1
#     j=0 # (1,0)
#     j=1 # (1,1)
#     j=2 #(1,2)
#     j=3 #-
# i=2 #...

n=4
for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
    print()
    
n=3
for i in range(3,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
print("*"*3)

for i in range(4):
    print("*"*i)
    
n=4
for i in range(0,n): #3
    print(" "*(n-i) + "*"*i)  

n=5    
for i in range(0,n):
    for j in range(n-i): # 5-0 5-1
        print(" ",end=" ")
    for k in range(i):
        print(" * ",end="")
    print()
    
a=[i*2 for i in range(6)]
print(a)

a=[]
for i in range(6):
    a.append(i)
print(a)

# 1.break
# 2.continue
# 3.pass

for i in range(6):
    pass

for i in range(6):
    print(i)
    if i==3:
        break
    
for i in range(6):
    if i==3:
        continue
    print(i)
    
a={"name":"apple","color":"Green","price":50}
# for i in a.keys():
#     print(i)
    
# for i in a.values():
#     print(i)

for k,v in a.items():
    print(k,"value=>",v)
    

for i in range(1,6):
    print(i)
    

for i in range(1,6):
    print(i)
    if i==3:
        break
else:   
    print("Run Succesfully")
    
# 1
# 12
# 123
# 1234

# 1
# 22
# 333
# 4444

n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    

#ord() & chr()

print(ord('A'))
print(chr(65))

for i in range(65,91):
    print(chr(i))

#enumerate

l=["apple","orange","banana"]
for index,i in enumerate(l,start=1):
    print(index,i)
   
# Output: 
# 1 apple
# 2 orange
# 3 banana
    
#Zip
a=["Rajesh","Ram","Nagaraj","Tamil"]
marks=[50,45,56]

print(list(zip(a,marks)))
#[('Rajesh', 50), ('Ram', 45), ('Nagaraj', 56)]