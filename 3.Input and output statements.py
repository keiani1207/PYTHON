boy_name = input("boy name = ")
girl_name=input("girl name = ")
boy_age = int(input("boy age = "))
girl_age =int(input("girl age = "))
# we use 'abs' because sometimes boy will be younger, so diff-of-age with negative symbol is inapporiate
age_diff = abs(boy_age - girl_age)
print(boy_name + " loves " + girl_name + ". age differnce is " + str(age_diff))
print(f"{boy_name} loves {girl_name}. age differnce is {age_diff}")
#hdc