# planina
import math
sum = 2
n = int(input("enter number : "))
for i in range(n):
    sum = sum + sum -1
    print(f"{i+1} | {sum} = {sum} + {sum} - 1 | {sum} = {math.pow(sum, 2)}")
print(math.pow(sum, 2))
