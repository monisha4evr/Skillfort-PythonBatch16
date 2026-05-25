#Conditional statement
# 1. if
# 2. nested if
# 3. if else
# 4. elif
# 5. match

#Syntax
# if condition:
    # logic
    

age=13
if age>=18:
    print("Eligible to Vote")
else :
    print("not Eligible")
    
password=int(input("Enter Password in number"))
if password == 123:
    print("Success")
else:
    print("Wrong Password")
    
#Syntax
# if condition:
#     print()
# elif condition:
#     print() 
# else:
#     print()   

a=50
b=20
c=30

if a>b and a>c:
    print("a is Greater")
elif b>c:
    print("b is Greater")
else:
    print("c is Greater")


day="Friday"
match  day:
    case "monday":
        print("today is Monday")
    case "tuesday":
        print("Today is Tuesday")
    case _ :
        print("Good Day")

    
    


