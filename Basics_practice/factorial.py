def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

userInput = int(input("Please Enter A Non-Negative Number: "))

if userInput > 0:
    print("The Factorial of", userInput, "is", factorial(userInput))
else:
    print("Sorry, Please Enter a Positive Integer")
