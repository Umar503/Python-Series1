import random
cnumber = random.randint(1 ,10)
userInput = int(input("Enter Your Number: "))
if userInput > cnumber :
    print("The Computer Number is =" ,cnumber)
    print("Your Number Is Too High")
elif userInput < cnumber:
    print("The Computer Number is =" ,cnumber)
    print("Your Number is Small")
else:
    print("Mubarak Ho Ap jeet Chukay Hain Baandra ma 200 Guz ka plot--- The Number Is=",cnumber)