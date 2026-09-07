import keyword
user_input =input("Enter variable name to check = ")
if not user_input.isidentifier():
    print("invalid variable name entered!!\nTry again..")
elif keyword.iskeyword(user_input):
    print(f"invalid!!. '{user_input}' is a reserved keyword in python")
else:
    print(f"'{user_input}' is valid variable name")