from numpy import fmin


def fMin():
    lMin = []
    for i in range(3):
        n = int(input("enter number "+str(i +1)+" : "))
        lMin.append(n)
    a = min(lMin)
    print(f"min number is {a}")
fMin()