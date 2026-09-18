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
if not (maths>=70 and science>=70):
    print("eligible for admission")
else:
    print("not eligible for admission")
