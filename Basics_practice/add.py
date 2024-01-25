a = int(input("Enter Your Number:"))
b= 0
while a!=0:
    b += a % 10
    a //= 10
print(f"The Sum Of Digits Of the Given Integer Is : {b}")
 