# creating a tuple
s = ("a","d","h","k")
print(s)
w = ("s",2,34.43)
print(w)

#creating a single tuple
name =("sun",)
print(name)

#accessing tuple elements
name =("sun","moon","star")
print(name[1]) 
print(name[-1])

#slicing tuple
b =("a","b","c","d","e","f")
print(b[1:4])

# checking its type
b =("a","b","c","d","e","f")
print(type(b))

#type conversion of data types
y =("3","2","6","5")
print(tuple(int(y) for y in ("3","2","6","5")))

#type converting particular element
i = (4,5,2,1,9,6)
print((4,) + tuple(str(i) for i in (5,2))+ (1,9,6))
print(tuple(str(i) for i in (4,5,2)) +(1,9,6))

#converting list into tuple
print(tuple([2,5,3]))

print("hi")
