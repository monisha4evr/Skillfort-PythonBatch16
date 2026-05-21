str="apple"
print(str[::-1]) # elppa - Reverse the String
print(str[1:5]) #pple (n-1) - slicing start and ending Index
print(str[1]) #p - Indexing

print(str.capitalize()) #Apple
print(str.upper()) #APPLE
print(str.lower()) #apple
print(str.endswith('e')) #True
print(str.startswith("e")) #False


str="apple is my fav"
print(str.find("R")) #-1
print(str.index("R")) # Error
print(str.split())

str=['apple', 'is', 'my', 'fav']
print(" ".join(str))
