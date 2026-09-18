#Censor & Replace
x="python is bad! I hate bugs, but python is versatile."
y=x.replace("bad","great",1)
z=y.replace("hate","love")
a=z.upper()
print(a)

#Compound Interest / Balance Tracker
s=1000
s*=2
s-=350
s/=2
print(s)
print(type(s))

#Eligible for Admission Check
maths = int(input("math score = "))
science=int(input("science score = "))
total_marks=maths + science
print("eligible:",(maths>=70 and science>=70) or total_marks >160)

#Keyword & Character Finder
secret = "PythonProgramming2026"
y=input("enter the text or word = ")
print(y in secret)
print('x' not in secret)

#Bitwise Manipulation Challenge
a=12
b=5
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(a>>1)

