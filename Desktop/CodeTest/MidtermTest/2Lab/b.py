def R2L(n):
    while n > -1:
        print(' '*n + '#')
        n -= 1
R2L(5)

def L2R(n):
    i = 0
    while i < n+1:
        print(' '*i + '#')
        i += 1
L2R(5)