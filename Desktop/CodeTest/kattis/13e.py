# pot

import math
sum = 0
n = int(input("enter number : "))
for i in range(n):
    line = str(input("enter line : "))
    sum += int(math.pow(line[:len(line):]))
print(sum)