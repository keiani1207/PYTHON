# tuple are ordered immutable and we can duplicate elements
# creating a tuple
s = ("a","d","h","k")
print(s)
w = ("s",2,34.43)
print(w)
print(len(w))  #length of tuple

#creating a single tuple
name =("sun",)
print(name)

#nested tuple
u=(1,7,3,(5,0))
print(u)

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

#empty tuple()
m = () # m = tuple()
print(m)
print(type(m))

#SETSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#sets are unqiue,unordered,unindexed(not indexing),it can be mutable
i = {3,1,90}
print(i) #unorderd

print(set((36,0,90))) #creating sets with func-set()

#type checking 
print(type(i))

#empty set
b = set() # b={} nooo bcz it will become empty dict 
print(b)
print(type(b))

# union, intersection, difference, symmetric difference
v ={3,5,1}
p ={6,3,0}
print(v | p)
print(v & p)
print(v - p)
print(v ^ p)


r={5,"hi",9.5}
print(r)

# add
r.add(0)
print(r)

#remove
r.remove(5)
print(r)

#pop()
r.pop() # here we can't give arguments like lists because sets are unordered and unindexed
print(r) 