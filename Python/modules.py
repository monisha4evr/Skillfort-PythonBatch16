Modules:
    simply a file with a .py extension that contains 
    code—like functions, classes, or variables
    - intended for reuse in other programs
3 types:
    built-in (math, os,dateTime)
    user-Defined (.py Files)
    external (numPy,Pandas,request...)
    

import datetime
cur_date=datetime.datetime.now()
print(cur_date.strftime("%y%m"))
print(cur_date.strftime("%d-%m-%y"))

date_string = "25-12-2026"
print(datetime.datetime.strptime(date_string,))

print(round(5.6))    
import math

print(math.round(5))
math.ceil(x): Rounds a number up to the nearest integer.
math.floor(x): Rounds a number down to the nearest integer.
math.trunc(x): Drops the fractional part, returning the integer part.
math.fabs(x): Returns the absolute float value of a number.
math.factorial(n): Returns the factorial of a positive integer.


File Handling:
----------------


var=open("mm.txt",'w') # write => Overwrite older content
var.write("\nWelcome to India")
var.close()

var=open("mm.txt",'a') # append => Append at end
var.write("\nWelcome to India")
var.close()

var=open("mm.txt",'r')
print(var.read())
var.close()

var=open("mm.txt",'r')
print(var.readline())
var.close()

var=open("mm.txt",'r')
print(var.readlines())
var.close()

with open("mm.txt",'r') as f:
    print(f.read()) 
    
    
#Exception Handling
#--------------------

a=5
b=0
try:
    c=5/2
    #d=int("abc")
# except ZeroDivisionError:
#     print("Cant divide by zero")
# except ValueError:
#     print("Cant convert")
except Exception as e:
    print(e)
else:
    print("I run only if no Errors")
finally:
    print("I run Always")


#--------------------------------    
def withdraw_money(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds for this withdrawal.")
    return balance - amount

try:
    current_balance = withdraw_money(50, 100)
except ValueError as error:
    print(f"Transaction Failed: {error}")
    
#---------------   
IndexError: Trying to access a list index that doesn't exist.
KeyError: A dictionary key is not found.
TypeError: An operation is applied to an object of inappropriate type (e.g., adding a string to an integer).
ValueError: A function receives an argument of the right type but inappropriate value.
FileNotFoundError: Attempting to open a file that does not exist at the specified path


print(dir(locals()['__builtins__']))

def userData(age,userId,userName,d=10):
    print(age,userId,userName,d)

print('------------------------------------')

userData(userId = 102, age = 22, userName = 'Priya')

def check_age(age):
    if age<0:
        raise ValueError("No")
        
try:
    check_age(-5)
except ValueError as error:
    print(f"Error caught: {error}")
