'''
try:
    input = int(input("Enter an number please"))
    print(input**2)
except ValueError:
    print("enter an int type number please")
'''
'''
try:
    name=str(input("Enter your name: "))
    age=int(input("Enter your age: "))
    if age>18:
        print(f"You can go.")
    else:
        print("We are sorry, but you are not old enough")
except ValueError:
    print("enter an int type number please")
'''


'''
try:
    first_number=int(input("Enter first number :"))
    second_number=int(input("Enter second number :"))
    answer=first_number/second_number
    print(answer)
except ZeroDivisionError:
    print("0 can not be divided")
'''
'''
with open("text.txt","w") as fileHandler:
    fileHandler.write("Pupsik")
try:
    with open("text.txt","r") as fileHandler:
        print(fileHandler.read())
except Exception:
    print("Sorry but we couldn't find or open this file ")
'''
'''
try:
    name=input("Enter your name :")
    name.capitalize()
except TypeError:
    print("You entered not a str type value, please fix it")
'''
