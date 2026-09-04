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

#combining the nested tuples
u=(6,9,0,9,6,(4,2,1))
print(u[:5] + u[5])
print(u[:5] + u[5][1:2])
print(u)

# u can concatate tuple to tuple only
u=(6,9,0,9,6,tuple([4,2,1]))
print(u[:5] + u[5])
print(u[:5] + u[5][1:2])
#or
print(u[:5] + (u[5][1],))

k=(6,9,0,9,6,[4,2,0,1])
print(k[:5] + (k[5],))

# repitation of tuple
d =(1,2,1,2)
print(d*3)

# count()
print(d.count(2))

# index()
print(d.index(2))

#operator
t=(4,9,2,3)
print(4 in t)

c = ("hi","hello","jkk")
print("hi" in c)

# concantination
z=("hg","lo")
i=("aq","ek")
print(z + i)