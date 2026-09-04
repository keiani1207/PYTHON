#creating a list
my_list = [1,"a",[2,5,"d"]]
print(my_list)

#accessing list elements
print(my_list[1])
print(my_list[-1])

#changing specific element
my_list[1] = "bd"
print(my_list)

#append - adding item in the end of the list
my_list.append(7)
print(my_list)
w=[1,2,5,4]
w.append([2,4])
print(w)

#If you want to keep the original list unchanged while creating a new one with the added item, you can use the addition operator (+)
w=[1,2,0.5,9,4]
print(w + [5])
d =[1,3,9,7,5]
print(d + [6,4] + [0])

#Method 1: Using Slicing (Recommended)
#You can split the list around the target index, add the new element in the middle, and join them together using the + operator
# a[:index] + [value] + a[index:]
a = ["hi",45,0.5,"a"]
print(a[:2] + ['B'] + a[2:])

#Method 2: Copying then Inserting
#Alternatively, you can make a duplicate of the list and use the standard insert() method on the copy, so the original stays untouched
q = ["hi",45,0.5,"a"]
q_new = q.copy()
q_new.insert(2,6)
print(q)
print(q_new)

#insert - inserting the element in a specific place
my_list.insert(1,'apple')
print(my_list)

##Method 2: Copying then removing
#Alternatively, you can make a duplicate of the list and use the standard remove() method on the copy, so the original stays untouched
o = ["hi",45,0.5,"a"]
o_new = o.copy()
o_new.remove("hi")
print(o_new)
print(o)

#remove - removes the specific element
my_list.remove('''apple''')
print(my_list)

#pop - removes the element, we have to mention particular index, if not - it removes last element in list
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)

#clear - removes all the elements from list 
my_list.clear()
print(my_list)

#slicing lists
s =[700,200,100,500,900,600,900]
print(s[1:4])
print(s[::2])

#length of list
print(len(s))

#sorted - returns a new sorted list without changing the original list
print(sorted(s))
print(s) 

#sum() - sum of elements in list
print(sum(s))

#index(element) - Returns the index number of the specified element.
print(s.index(900))

#count(element) - Returns the number of occurrences of an element in the list.
print(s.count(700))

#reverse() - Reverses the elements of the list 
s.reverse()
print(s)

#sort() - Sorts the list in place (ascending by default).
s.sort()
print(s)

#extend() 
w=[1,2,5,4]
w.extend([2,4])
print(w)

numbers = [5, 2, 9, 1,"jskd",[2,4,7,0]]
print(len(numbers))

# desending order
v=[9,6,8,3,1]
v.sort()
v.reverse()
print(v)

#nested list (matrix) and accessing of nested lists
r =[[1,2,3],
    [4,5,6],
    [7,8,9]]
print(r)
print(r[0:2])
print(r[0][1])
print(r[0][0:2])

#ENG IN KANNADA PROJECT
c =[900,800,700,600,500]
c.append(90)
print(c)
c.insert(2,300)
print(c)
c.pop(2)
print(c)

#type checking
print(type(c))

# converting tuple to list
p=("h","e","l")
print(list(p))
# or
print(list((p)))
print(p)

p=("h","e","l",["l","o"])
print(list(p))

g =["p","h","y",("t","o","n")]
print(g[0:3] + [g[3]])

r=["p","h","y",list(("t","o","n"))]
print(r[0:3] + r[3])

# combining 2 lists
n =[1,3,9,[6,4,0]]
print(n[:3]+n[3])
print(n[:3] + n[3][1:2]) 
print(n[:3] + [n[3][1]])

#type conversions
t =[2,6,4,3]
print(list(str(t) for t in [2,6,4,3]))
print([t[0]]+ list(str(t) for t in [6,4]) + [t[3]])

#opertor
c=[4,9,1,0]
print(4 in c)

j=["hi","hw"]
print("ho" in j)

