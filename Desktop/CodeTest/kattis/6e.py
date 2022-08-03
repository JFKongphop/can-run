# Take Two Stones
n = int(input("enter stones number : "))
for i in range(n):
    if i+1 < n:
        n -= i
    else:
        print(n)
        if n % 2 == 0:
            print("Bob")
        else:
            print("Alice")
        break