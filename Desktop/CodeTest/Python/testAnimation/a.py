from blessings import Terminal
term = Terminal()
print(term.move(3,4),"*")
print(term.move(6,7),"*")

print("kongphop")

# import os
# import sys
# import numpy as np

# def get_string(pattern, num):
#     string = ""
#     for i in range(num):
#         for j in range(num):
#             if pattern[i][j] == 0:
#                 string += "   "
#             else:
#                 string += " * "
#         string += "\n"
#     return string


# num = 5
# pattern = np.zeros((num, num))

# loc = (num // 2)
# pattern[loc, loc] = 1
# string = get_string(pattern, num)
# os.system("clear")
# sys.stdout.write("\r" + string)
# sys.stdout.flush()


# for k in range(1, loc+1):
#     for i in range(num):
#         for j in range(num):
#             eclu = abs(i - loc) + abs(j - loc)
#             if eclu == k:
#                 pattern[i, j] = 1
#     string = get_string(pattern, num)
#     os.system("clear")
#     sys.stdout.write("\r" + string)
#     sys.stdout.flush()