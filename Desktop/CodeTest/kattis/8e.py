# Sort Two Numbers
a = list()
for i in range(2):
    n = int(input(f"enter number {i + 1} : "))
    a.append(n)

temp = 0
if a[0] > a[1]:
    temp = a[0]
    a[0] = a[1]
    a[1] = temp
    for i in a:
        print(i)