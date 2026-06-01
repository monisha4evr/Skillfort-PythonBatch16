# Function
# REusable block of Code to do some Specific Task

# Syntax:

# def function_name():
#     #Statement

#function_name()

def welcome():
    print("Welcome to Skillfort")
    
welcome()
welcome()
welcome()
welcome()

# 1. function without argument and without return
def test():
    print("This is Example for normal Function")
test()

# 2. function with argument and without Return

# Argument: actual vaLue
# parameter: Name used to get that value

def greet(a):
    print(f"Hi! {a}, Welcome to Skillfort")
    
name="praneesh"    
greet("tamil")
greet(name)

#3. function with argument and return

def add(a,b):
    return(a+b)

res=add(10,20)
print(res)

print(add(30,50))

#4.without argument with return

def multiply():
    a=10
    b=20
    return(a*b)
    
    
print(multiply())


# 1. Taking all remiaining value and makes it as tuple

def sud_det(name,*subject):
    print(name,subject)

sud_det("tamil","python","java","php")

# 2. Taking all remiaining  key value and makes it as Dict

def sud_det(name,**subject):
    print(name,subject)

sud_det("tamil",python=30,java=40,php="50")

# 3. example for Both
def student_details(name,*city,**extra):
    print(name,city,extra)
    
student_details("Tamil","chennai","python",sub="mm",result="pass")

def student_details(name,city,course):
    print("name=",name,"City=",city,"Course=",course)
    
student_details(city="chennai",name="Tamil",course="python")


def register_detail(user_name,password,default_user="user"):
    print(f"Username {user_name} ,defaul_user {default_user}")
    

register_detail("tamil",123)
register_detail("tamil",123,"tamilzhisai")


# Task2 : even list
#     [1,2,3,4,5]
    
# task3:  sort
#     [5,3,68,1,9,8]

# task 4. factorial 

# task 5. one sample for all types