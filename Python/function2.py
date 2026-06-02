#function 
#scope
# lamba Function
# map ,filter
# Generator
# Decorator
#modules
    # 1. Built-in Modules (math and random)
    # 2. User-Defined (Custom) Modules
    # 3. Third-Party Modules - request,numpy,pandas
# Exception Handling
# file Handling
# oops    


def registration(city,name="user"):
    print(name,city)
    
registration("chennai","Tamil")

def function_name(a,*b):
    print(a,b)
    
function_name(4,5,6,7)

def funcname(a,**b):
    print(b)

a=10
funcname(a,name="apple")


def sample_function(a,b):
    print(a,b)
b=2
sample_function("mm",b)


# Scope
# local Scope
# global Scope



x=10
def sample():
    x=20
    print(x)
    
sample()  
print(x)  


# lambda function  -> Ananymous function
# Syntax => lambda arguments: expression

square_lambda = lambda x: x * x
print(square_lambda(5))

a=10
print("Even" if a%2==0 else "odd")

a = [1, 2, 3, 4]

# Convert and execute using map()
result = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", a))

print(result)
# Output: ['Odd', 'Even', 'Odd', 'Even']


# Syntax: res=list(map(func,iterator))
# Syntax : res=list(filter(func,iterator))

a=[1,2,3,4]
res=map(lambda i:i*2,a)
print(list(res))



def fruit_name(a):
    print(a['name'])

frt={"name":"apple","color":"red"}

fruit_name(frt)

def fruit_name(a):
    print(a[0])

frt=['apple','orange']

fruit_name(frt)


#Generator

def func():
    x=10
    return 
    print(x)
    
func()

# it wont x value

def gen():
    yield 1
    yield 2
    yield 3
    
a=gen()
print(next(a))
a=gen()
print(next(a))


# Decorator

# A Python decorator is a function that takes another function as an argument, extends 
# its behavior without modifying its actual source code, and returns a new function

def mydecor(func):
    def inner():
        return func()
    return inner

@mydecor
def test():
    print("hi")
    
test()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Real time Usecase

# Logging: Tracking when functions are called and with what arguments.
# Timing & Benchmarking: Measuring code performance and function execution time.
# Authentication/Authorization: Verifying permissions before running web routing code.
# Caching & Memoization: Storing expensive API or calculation results to avoid redundant operations.
# Rate Limiting & Retries: Automatically retrying failed network requests
    
    
    
