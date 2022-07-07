def triR(n):
    j = 0
    i = 0
    while n > -1:
        print(' '*j + '#'*n)
        n -= 1 # n is number of # when print
        j += 1 # j is number of ' ' when print
triR(5)


