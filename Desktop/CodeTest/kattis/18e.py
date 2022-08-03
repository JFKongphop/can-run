# Jack-O'-Lantern Juxtaposition

n = int(input("enter times : "))
sumx = 1
for i in range(n):
    number = int(input(f"enter number {i+1} : "))
    sumx *= number
print(sumx)