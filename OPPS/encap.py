class Encap:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name
obj = Encap()
obj.setname("Umar")
result = obj.getname()
print(result)

