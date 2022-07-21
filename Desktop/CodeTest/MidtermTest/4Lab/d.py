def dTri(n):
    print("x"*n)
    if n > 1:
        dTri(n-1)
number = int(input("enter number : "))
dTri(number)