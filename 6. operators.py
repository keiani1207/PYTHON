#assignment operators
x = 5
x+=10
print(x)
x-=10
print(x)
x*=10
print(x)
x/=10
print(x)
x%=10
print(x)
x//=10
print(x)

#comparison operators
x = 10
print(x == 12)
print(x != 12)
print(x >= 12)
print(x <= 12)
print(x < 12)
print(x > 12)

age = int(input("Enter your age : "))
if(age>=18):
    print("You are an adult")
    if(age<18):
        print("Minor")

#logical operator
x=5
y=10
print(x<10 or y>12)
print(x>2 and x<12)
print(x>10 and y<5)
print(not(x<10))

a = int(input("a = "))
b = int(input("b = "))
print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>b))


#membership operator
my_list = [1,2,3,4,5]
my_string ="python"
print(3 in my_list)
print(7 in my_list)
print(7 not in my_list)
print("x" in my_string)
print("x" not in my_string)

q = input("enter a string = ")
print("a" in q)  
print("python" not in q)

#combining both membership and logical operator
x="hello world"
print(("h" in x) and ("d" in x))


#bitwise operator
r = 4
u = 8
print(r | u)
print(r & u)
print(r ^ u)
print(~r)
print(r<<1)
print(r>>1)

#identity operator
x="hello"
y="hello "
print(x is y)

s = "python "
t="python"
print(s is not t)