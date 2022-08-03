# Nasty Hacks
number = list()

def getAll():
    for i in range(3):
        bg = int(input("Enter number : "))
        number.append(bg)

n = int(input("enter round : "))
for i in  range(n):
    getAll()
    print(number)
    if len(number) == 3:
        if number[1] - number[2] > number[0]:
            print("Advertise")
        elif number[1] - number[2] == number[0]:
            print("Dose not metter")
        else:
            print("Do not advertise")
    else:
        continue
    number.clear()   
    print(number) 
    

    