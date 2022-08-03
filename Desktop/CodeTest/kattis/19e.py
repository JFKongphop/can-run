# heart rates
n = int(input("enter number : "))
for i in range(n):
    b = int(input("enter beat : "))
    p = float(input("enter second : "))
    heartRate = (60*b) / p
    print(round(heartRate, 4))