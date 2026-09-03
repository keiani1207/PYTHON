# varaible assignment
a = 10
b = 20
c = 30
print("a = ",a)
print("b = ",b)
print("c = ",c)

a,b,c = 40,50,60
print("a = ",a)
print("b = ",b)
print("c = ",c)

a=b=c=80
print("a = ",a)
print("b = ",b)
print("c = ",c)

#data types
x = 20
y = "python"
z = 84.56
switch_on = False
d = None
print(type(x))
print(type(y))
print(type(z))
print(type(switch_on))
print(type(d))

#type conversion
x = float(x)
print(x)
print(float(89))
j=34
print(float(j))
print(j)

#type conversion and addition 
age = 22
num = "100"
print((int(num)) + age )

#printing mutiple varaibles using single print function(f-strings or formatted strings)
name = "xyz"
age = 22
collage ="abc"
print(f"name = {name}, age = {age}, collage = {collage}")
print(name,age,collage)
print(f"{name}\n{age}\n{collage}")

# arthematic operations 
a,b = 3,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor divison
print(a%b)  #modulus
print(a**b) #exponent(3**2 = 9) 

# combining different operators
print(10+8/2*3)
print(25//4+3*2)

#swaping varaibles
a = 10
b = 20
a,b=b,a
print(a)
print(b)

