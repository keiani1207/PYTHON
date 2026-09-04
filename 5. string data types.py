# different types of escape sequence 
# 1. single quote - \'
print('it\'s alright')
print("it\"s alright")
print("chandan said \"hi\" to darshan")
# 2. carriage return
print("python\rJava")

# 3. backspace
print("hello\bworld")

# different string methods
# 1. capitalize() - make the first character of the entire string uppercase and make everything else lowercase
a = "welcome home!!"
print(a.capitalize())
b = '''this is apple.
this is pineapple'''
print(b.capitalize())
print("DGGTD".capitalize())

# 2. centre() - places a string in centre of a given width by adding spaces or another character around it.
text = "hello"
print(text.center(11))  #hello has 5 characters, 11-5 = 6 so 3 space right and 3 space left, if in case we give 12 instead of 11, spaces become 7 then 3 space on left and 4 space of right 
print(text.center(11,"*"))
print("ASDFG".center(12,'@'))

# 3. count() - The count() method returns the number of times a specified value appears in the string.
print("i love apple, apple are my fav. apple are sweet".count("s"))
print("i love apple, apple are my fav. apple are sweet".count("apple"))
print("banana".count("a",2,6))

# 4. endswith() - it is a python string method that checks whether a string ends with a particular character or word. it returns true or false.
print("hello.".endswith("."))
print("hello.3".endswith("3",0,3))
print("hello.3".endswith("."))

# 5. find() - in Python is a string method used to find the position (index) where a specified substring starts inside a string.
print("hi python world".find("python"))
print("hello python".find("java"))  #find() returns -1 when the specified substring is not found in the string.
print("banana".find("a",2,))
print("banana".find("a",2,3))

# 6. format() - in Python is used to insert values into a string at specified positions/placeholders.
print("my name is {},my age is {}.".format("shravani",19)) #basic positional arguments
print("my name is {1},my age is {0}.".format(19,"shravani")) #indexed argumnets
print("my name is {name},my age is {age}.".format(name = "shravani",age = 19)) #keyword arguments

# 7. index() - In Python, the .index() method is identical to .find() in searching for a substring and accepting optional start and end arguments, but differs by raising a "ValueError" if the substring is missing instead of returning -1.
print("hello python".index("python"))
'''Why use .index() instead of .find()?
You use .index() when the presence of the substring is mandatory for your code to work. If it's missing, you want the program to stop and throw an error immediately rather than silently failing and passing -1 into the rest of your code.'''
print("banana".index("a",2))

# 8. isalnum() method checks whether all characters in a string are alphanumeric (meaning they are either letters or numbers) and returns a boolean (True or False).
print("ndnsk38".isalnum()) #true
print("2".isalnum()) #true
print("hi hello".isalnum()) #false
print("résumé".isalnum())  #Unicode letters like é are accepted #true
print("éñüçåприветγειαمرحبا".isalnum()) #true
print("½".isalnum()) #Unicode fraction characters are also considered #true
print("²".isalnum()) #true
print("Ⅷ".isalnum()) #true

# 9. isalpha() method checks whether all characters in a string are alphabetic (meaning only letters from the alphabet, with no numbers, spaces, or symbols) and returns a boolean (True or False).
print("hgsins ".isalpha()) #false
print("résumé".isalpha()) #true
print("éñüçåприветγειαمرحبا".isalpha()) #Unicode letters like é are accepted #true

# 10. isascii() - .isascii() method checks whether all characters in a string are ASCII characters (meaning they fall within the standard range of code points from 0 to 127, covering standard English letters, numbers, and basic punctuation) and returns a boolean (True or False).
print("hxb4!!".isascii()) #true
print("résumé".isascii()) #false

# 11. isdecimal() - .isdecimal() method checks whether all characters in a string are base-10 decimal characters (digits 0 through 9), returning a boolean (True or False).  
print("233".isdecimal()) #true
print("٠١٢٣٤".isdecimal()) # Output: True (Arabic-Indic decimal digits are also recognized) #true
print("123.456".isdecimal()) #false
print("²".isdecimal()) #false
print("½".isdecimal()) #false
print("Ⅷ".isdecimal()) #false

# 12. .isdigit() method checks whether all characters in a string are digits and returns a boolean (True or False).
print("1223".isdigit()) #true
print("²".isdigit()) # Superscript 2 is considered a digit #true
print("12.345".isdigit()) #false
print("½".isdigit()) #false
print("Ⅷ".isdigit()) #false

# 13. isidentifier() method checks whether a string is a valid identifier (meaning it can legally be used as a variable name, function name, or class name in Python code), returning a boolean (True or False).
print("1asgg_12".isidentifier())
print("if_12".isidentifier())

# 14. .islower() method checks whether all cased characters in a string are lowercase and whether there is at least one cased character, returning a boolean (True or False).
print("bhqwdodh".islower()) #true
print("1233@@".islower()) #false
print("oG123".islower()) #false

# 15. isnumeric() method checks whether all characters in a string are numeric characters and returns a boolean (True or False).
print("1234".isnumeric()) #true
print("hdhhd".isnumeric()) #false
print("½".isnumeric()) # Output: True (Fractions are numeric)
print("²".isnumeric())   # Output: True (Superscripts are numeric)
print("Ⅷ".isnumeric())   # Output: True (Roman numerals are numeric)

# 16. isprintable() method checks whether all characters in a string are considered "printable" (meaning they occupy space on a screen or can be rendered visibly) and returns a boolean (True or False).
print("hello\rhi".isprintable())  # false
print("hello world".isprintable()) # true 

# 17. isspace() method checks whether all characters in a string are whitespace characters (spaces, tabs, newlines, etc.) and returns a boolean (True or False).
print("\n".isspace()) #true
print("jzjxsi".isspace()) #false
print("\r".isspace()) #true
print("\n\r\t".isspace()) #true

# 18. istitle() - it is a method checks whether a string is formatted in title case (meaning every word starts with an uppercase letter, followed only by lowercase letters) and returns a boolean (True or False).
print("Hello hi ".istitle()) # false
print("Welcome To Python".istitle()) # true

'''title() takes your string and transforms it, returning a new string.

.istitle() looks at your string and returns a boolean (True or False) telling you whether it's already properly capitalized.'''

# 19. isupper() - it is a method checks whether all cased characters in a string are uppercase and whether there is at least one cased character, returning a boolean (True or False).
print("JHWJGHREIOEJ".isupper()) #true
print("F55gg83674@@@".isupper()) #false
print("6748@&".isupper()) #false

# 20. ljust() pads the right side of a string with spaces (or a specific character) to make sure the overall string reaches a specified total width.
print("hello ".ljust(7,"-"))

# 21. lower() method converts all uppercase characters in a string into lowercase and returns the new string.
print("d6HWDOWDk".lower())

# 22. lstrip() method removes leading characters (characters on the left side of a string) and returns the modified string.
print("        hello world          ".lstrip())
print("@@@@@hello world@@@@@".lstrip("@"))

# 23. replace()
print("hello python".replace("python","Java"))
print("banana".replace("a","o"))
print("banana".replace("a","o",1)) # Replace only the first 'a'
print("banana".replace("a","o",2)) # Replace the first two 'a's

# 24. rfind() - find the position (index) of the last occurrence of a substring inside a string.
print("hello world hello".rfind("hello"))
print("banana".rfind("a",0,4))

# 25. rindex() - find the position (index) of the last occurrence of a substring inside a string.
print("hello world hello".rindex("hello")) # rindex() and rfind() both are same but The important difference is, the output it gives - when the word is not found
print("banana".rindex("a",0,4))

# 26. rjust() → moves/keeps the text on the RIGHT by adding space/characters on the LEFT.
print("hello".rjust(11,"#"))

# 27. rsplit() - Splits the string at the specified separator, and returns a list. and split from right
print("hi-hello-everyone".rsplit("-",1))
print("hihelloeveryone  mypython".rsplit(" ",1))

# 28. rstrip() - remove characters/whitespace from the right side (end) of a string. and rstrip() removes all matching characters from the right side until it reaches a different character.
print("hellooooooooo".rstrip("o"))

# 29. split() - Splits the string at the specified separator, and returns a list. and split from left
print("hi-helloeveryone ,, 123".split("-"))
print("hi-helloeveryone ,, 123".split())
print("hi helloeveryone ,, 123".split(" ",1))

# 30. startswith() - checks whether a string starts with a specified character or substring. It returns True if it starts with it, otherwise False.
print("hello hi everyone".startswith("hello"))
print(" hi hello hello everyone hello".startswith(" "))
print("hello everyone hello".startswith("e",6))

# 31. strip() method removes leading and trailing characters (from both the left and right sides of a string) and returns the modified string.
print("  hello hi".strip())
print("##   hello hi   ##".strip("#"))

# 32. swapcase() - changes uppercase letters to lowercase and lowercase letters to uppercase.
print("Hi".swapcase())

# 33. title() - converts the first letter of every word to uppercase and the remaining letters to lowercase.
print("hi HELLO evERyone!!".title())

# 34. upper() method converts all lowercase characters in a string to uppercase and returns a brand-new modified string.
print("hello".upper())

#convert string to list/tuple
y = "hi"
print(list(y))
print(tuple(y))

r ="hi,ho,hello"
print(r.split(","))
print(r)
s = r.split(",")
print(tuple(s))

h="hi,he,she.d"
p=h.replace(".",",")
g=p.split(",")
print(g)
print(tuple(g))

r ="hi,ho,hello"
print(tuple(r))