i = int(input())
j = int(input())
if i> 0 and j> 0:
    for k in range(1, j+1):
        for x in range(k, i+1, j):
            print(x, end=" ")
        print()
else:
    print("Invalid input")

# i = int(input("enter i : "))
# j = int(input("enter j : "))

# if i > 0 and j > 0:
#     n = 1
#     m = 0
#     while n < j+1:
#         while m < i + 1:
#             print(m, end=" ")
#             m += j
#         print()
#         n += 1
# else : print("invalid")

