#repitation
message = "python "
print(message * 3)

#repitation 
message = "python "*2
print(message)
print("hi "*3)

#string methods
word = "prOgrAmmIng"
sen = "       python programming    "
print(word.upper())
print(word.lower())
print(sen.strip())
print(sen.replace("python","C"))

#string operation with quotes
a = "chandan said 'hi'"
print(a)
b = 'chandan said "hi"'
print(b)
c = "chandan said 'hi' darshan said 'hello' "
print(c)
# for multi-line string use triple qoutes compulsary ''' ''' or """ """
d = """a said 'b' 
b said 'c' """
print(d)
e = "e said 'f'\nf said 'g' "
print(e)
x ="x said '''y'''  y said 'z' "
print(x)
q = """p said 'r' 
k said "v" """
print(q)

# length of string
a = "GOOD MORNING"
print(len(a))

#accessing single string characters
c = "chandan"
print(c[4])  # index = position - 1
print(c[2])
print(c[-2])

#accessing substrings
c ="chandan"
print(c[2:7])
print(c[:3])
print(c[2:5])
print(c[-4:-1])
print(c[-1:-4]) # output will be empty string because by default it will take +1 and tries to move forward but after -1 there is ntg so empty string will be a output
print(c[-1:-4:-1])
print(c[::2])
print(c[::3])
print(c[::-1])
print(c[::-2])
print(c[:6:2])
print(c[1:5:3])
print(c[-1:])
print(c[-5:-1:2])

#small project from engineering in kannada 3b notes
senten = input('sen =  jdjd      ') # here "sen = jdjd" basically a prompt. In the context of input(), a prompt is any msg displayed to the user asking them to enter input. but remember not every msg displayed by a program is a prompt ex: print("welcome")  welcome is an output, not a prompt 
print(senten.upper())    
print(senten.lower()) 
print(senten)
print(senten.replace(" ","_"))
print(senten.strip())
# see here "jdjd" is not converting into upper() lower() and all because variable takes only user input for processing not prompt 

# small project
xyz = input("text = ")
pqr=(xyz.replace(" ",""))
print(len(pqr))

# escape sequence
print("hello\n\twrold")
print ("this is a blacklash : \\")

o = "appl"
print(o + ("e"))

g = "yu"
print(g[:1] + ("o") + g[1:])
