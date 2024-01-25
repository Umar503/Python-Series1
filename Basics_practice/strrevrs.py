umar_str = input("Enter YOur String Here To reverse it :")
reverse_str = umar_str[::-1]
print(reverse_str)
# Question 2: Write a Python program that takes two strings as input from the user and
# returns True if both strings are anagrams of each other, otherwise return False. Anagram
umar_str1 = input("Enter First String : ")
umar_str2 = input("Enter Second String : ")
if sorted(umar_str1) == sorted(umar_str2):
    print(True)
else:
    print(False)
     