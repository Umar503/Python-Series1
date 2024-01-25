
# This Shows the error because i Am Trying to access the prtected member of the class
# class Student:
#     __name = "Umar"
#     def __init__(self) -> None:
#         pass

# obj = Student()
# print(obj.__name)



class Student:
    __name = "Umar"
    def __init__(self):
        print(self.__name)
        self.Displayinfo()
    def Displayinfo(self):
        print("Welcome Mr:Umar")

obj = Student()





