# input and Output Operation:

# Output 
# Type 1 Only String
print("Hello World") # Print whatever inside the Double Quotes
#output: Hello World

# Type 2 String + Variable
name="Arun"
age=25
print("Name = ",name,"Age =",age)
#Output : Name =  Arun Age = 25

#Type 3 Format String
print(f"Name: {name}\nAge: {age}")
"""
Output :
    Name: Arun
    Age: 25
    """

# input String 
a = input("Enter a value")
print(a)
"""
Output:
    Enter a valuemm
    mm
    """
# Data type
# id() and type() methods

a = 123
print(type(a))  # int
print(id(a)) #memory address

a = "qwr"
print(type(a)) # str
print(id(a))

a= True
print(type(a))  # bool
print(id(a))

a = 12.2
print(type(a)) #float
print(id(a))

a = 3 + 4j
print(type(a))  # complex 
    
a=[1,2,3]
print(type(a))  # List 

a=(1,2,3)
print(type(a))  # <class 'tuple'> 
print(id(a)) 

a={1,2,3}
print(type(a))  # <class 'set'> 

a={"name":"apple"}
print(type(a))  # <class 'dict'> 

# implicit Type Conversion
a=10 #type - int
b=10.5 #type - Float
c=a+b #type - Float automatically convert int to float

a=5 #int
b=5 #int
c=a/b #float

#explicit Type Conversion
a="123"   # str
b=int(a)  # int

a=(1,2,3)
b=list(a)
print(b)
print(tuple(b))



a=[1,2,3,4]
print(5  in a)
