# 1. For loop
# 2. While Loop

#output : 1 2 3 4 5 
i=1
while i<=5:  # 1<=5 T  2<=5 T 3<=5 =T  4<=5 =T 5<=5 =T 6<=5=F
    print(i)  # 1  2 3 4 5
    i=i+1 # 1+1 =2 2+1=3 i=3  3+1=4 4+1 =5 5+1=6
    #i+=1
    
i=1
while i<=5:  #1<=5 T  3<=5 T 5<=5 T 7<=5 F
    print(i)  #1 3 5
    i+=2    # 1+2=3   3+2=5 5+2=7
    
# output : 5 4 3 2 1

i=5
while i>=1 :  # 5>=1 T  4>=1 T  3>=1 T  2>=1 T 1>=1 T 0>=1 F
    print(i,end=" ") # 5 4 3 2 1
    i-=1 #  5-1 =4  4-1 =3 3-1 =2 2-1 = 1  1-1 = 0

a=123  #output 321
rev=0
while a>0: #123  12>0 T  1>0 T  F
    r=a%10  # 3  12=> 2  1%10 1
    rev= rev*10+r   #rev=3   3*10+2 = 32   32*10+1  320+1 321
    a=a//10 # 123//10 = a= 12  12//10 = 1  1//10
print(rev)
    
    
# for

#Syntax: range(start,end,step)

for i in range(1,5):
    print(i)
    
for i in range(5,1,-1):
    print(i)
    
a=[1,9,3,5]
for i in a:
    print(i)
    
    
a=[12,4,7,3,9,8]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
print(even)


str1="madam"
rev=''
for i in str1:
    rev=i+rev
if rev==str1:
    print("palindrom")
else:
    print("not a palindrom")


