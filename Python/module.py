#modules
    # 1. Built-in Modules (math and random)
    # 2. User-Defined (Custom) Modules
    # 3. Third-Party Modules - request,numpy,pandas
# Exception Handling
# file Handling

import math
print(math.sqrt(25))
print(math.ceil(25.6))
print(math.ceil(25.1))
print(math.floor(25.1))
print(math.floor(25.6))

a=10.6
print(round(a))

import datetime
print(datetime.datetime.now())
cur_date=datetime.datetime.now()
print(cur_date.year)
print(type(cur_date))

from calculation import add,mul
print(add(5,3))
print(mul(5,3))


# Exception Handling
# try
# except
# else
# finally

# except:
1. Generic Error
2. Specific Error



try:
    a="hi"+5
except TypeError:
    print("Can't Add Number With String")
except ValueError:
    print("Values")
    
try:
    a="hi"+5
except (TypeError,ValueError) as error:
    print("Can't Add Number With String",error)
    
try:
    a=5/0
except Exception as error:
    print("Error",error)
    
try:
    a=5/2
except Exception as error:
    print("Error",error)
else:
    print("There is no error")
    
try:
    a=5/2
except Exception as error:
    print("Error",error)
else:
    print("There is no error")
finally:
    print("I excecute irrespective of errors")    
    
# raise 

def check_age(a):
    if a<0:
        raise ValueError("Age must be grater than 0")
    
try:
    check_age(-3)
except ValueError as e:
    print("Error",e)

#File Handling 

# open("url",mode)

# read => r
# write => w
# append => a

file=open("tamil.txt",'w')
file.write("Welcome\n TO Skillfort")
file.close()

file=open("tamil.txt",'a')
file.write("\n Happy Learning")
file.close()

with open("mm.txt","w") as f:
    f.write("hi")
    
with open("tamil.txt",'r')as f:
    print(f.read())

with open("tamil.txt",'r') as f:
    print(f.readline())
    
with open("tamil.txt",'r') as f:
    print(f.readlines())


    
    






