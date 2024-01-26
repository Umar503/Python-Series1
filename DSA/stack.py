list = []
while True:
    c = int(input('''

                  1 Push Element
                  2 Pop Element
                  3 Peek Element
                  4 Display Stack
                  5 Exit


'''))
    if c==1:
        num=int(input("Enter the number to be added : "))
        list.append(num)
    elif c==2:
        if len(list) ==0:
            print("Stack is empty")
        else:
            p = list.pop()
            print("The element removed from stack is ",p)
        
    elif c==3:
        if len(list)==0:
            print("Stack is Empty")
        else:
            print("Top of the Stack is ",list[-1])
    elif c==4:
        print("Display Stack :" ,list)
    elif c==5:
        break
    else:
        print("Invalid Choice, Please Enter Again ")



    