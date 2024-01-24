"""
Multiplication Table Generator

This script takes a number as input and prints its multiplication table from 1 to 10.
"""

a = int(input("Enter Your Number:"))
print(f"The Table of {a} is:")
for i in range(1, 10):
    print(f"{a} x {i+1} = {a*i}")
