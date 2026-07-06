str="apple"
print(str[::-1]) # elppa - Reverse the String
print(str[1:5]) #pple (n-1) - slicing start and ending Index
print(str[1]) #p - Indexing
print(str[4:1:-2]) #ep


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

str="python"
new=str[2::]+str[:2]
print(new)
print(["presernt" if str in new else "not present"])

a="python"
print(a[::-1])
print(a[6:0:-2])
print(a[2:3])

print("Hi" * 3)  # 'HiHiHi'
print("Hi" * 0)  # ''

str="flower"
print(str.upper())

s=["Apple","Orange","Banana"]
s.sort()
m=sorted(s)
print(s,m)

