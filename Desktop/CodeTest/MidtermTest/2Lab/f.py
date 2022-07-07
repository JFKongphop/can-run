def minmax():
    linA = []
    minx = 0
    while True:
        n = input("enter number : ")
        if n == '$':
            print(f"min number is : {min(linA)}")
            print(f"max number is : {max(linA)}")
            break
        linA.append(n)
minmax()
