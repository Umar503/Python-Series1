list = []
while True:
    c = int(input('''
                  1 Enqueue
                  2 Dequeue
                  3 Front Queue
                  4 Rear Queue
                  5 Display
                  6 Exit

'''))
    if c == 1:
        x = input("Enter the element to be added : ")
        list.append(x)
    elif c == 2:
        if len(list) == 0:
            print("Queue is Empty")
        else:
            print("Element Removed from Queue : ", list.pop(0))
    elif c == 3:
        print("The front Element of the Queue is :" ,list[0])
    elif c == 4:
        print("The rear Element of the Queue is :", list[-1])
    elif c == 5:
        if len(list) == 0:
            print("Queue is Empty")
        else:
            print("Queue Is :",list)
    
    elif c == 6:
        break
    else:
        print("Invalid Choice, Please Enter Again ")

       