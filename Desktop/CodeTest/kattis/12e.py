# Quadrant Selection
a = list()
for i in range(2):
    x = int(input("enter x : "))
    y = int(input("enter y : "))
    if (x > -1000 and x < 1000 and x != 0) and (y > -1000 and y < 1000 and y != 0):
        if(x > 0 and y > 0):
            print("1")
        elif(x < 0 and y > 0):
            print("2")
        elif(x < 0 and y < 0):
            print("3")
        else:
            print("4")
        break
    else:
        print("invalid")
        break