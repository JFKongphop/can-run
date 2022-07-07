def backward(n):
    if n > -1 and n < 21:
        for i in range(n, -1, -1):
            print(i)
    else: print("invalid")
backward(-9)