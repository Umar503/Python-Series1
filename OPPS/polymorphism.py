

#Function OverRiding
class A:
    def dislplayInfo(self):
        print("Welcome To Jumanji")
class B(A):
    def dislplayInfo(self):
     #agr hum parent walay function to b call karna chaa rhy hain to hmain super function use karna pary ga
     # like This     super().displayInfo()
     print("Welcome To Jungle")
       

obj=B()
obj.dislplayInfo()


#Function OverLoading

class Umar:
    def greetings(self,name=""):
        print("Welcome MR:"+ name)
obj = Umar()
#Same Function Name Ha lekin 2 different kaam kr rha ha and this is call function overloading
obj.greetings()
obj.greetings("Programmer")