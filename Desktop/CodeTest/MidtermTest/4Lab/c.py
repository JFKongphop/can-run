def fAvg():
    sumx = 0
    i = 0
    while i < 3:
        n = int(input(f"enter number {i + 1} : "))
        sumx += n
        i += 1
    avg = sumx/3
    print(avg)
fAvg()

