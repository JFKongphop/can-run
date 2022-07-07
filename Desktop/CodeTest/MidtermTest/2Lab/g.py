def factor(n):
    i = 1
    while i < n+1:
        if n % i == 0:
            print(i)
        i += 1
factor(30)

