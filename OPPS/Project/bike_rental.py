class BikeStore:
    def __init__(self,stock) -> None:
        self.stock = stock
    def displayBikes(self):
        print("Total Bikes Available:",self.stock)
    def RentBike(self,q):
        if q<=0 or q>self.stock:
            return "Invalid Quantity"
        else:
            print("Total Price:",q*100)
            self.stock -= q
            print("Remaining Bikes:",self.stock)
while  True:
    obj = BikeStore(100)
    uc = int(input('''
1 : Display Stock
2 : Rent a Bike
3 : Quit

'''))
    if uc == 1:
        obj.displayBikes()
    elif uc == 2:
        b = int(input("Enter the number of Bikes you want to rent:"))
        obj.RentBike(b)
    elif uc == 3:
        break
    
    
    