# Quality-Adjusted Life-Year
def check(n, decimals):
    if type(n) == "float" or type(n) == "int":
        # will change when after . that have only 0 or not have
        sb = str(n)
        ns = len(sb)
        indexNS = 0
        for i in range(ns):
            if sb[i] == ".":
                indexNS = i

        cutBefore = ""
        for i in range(ns):
            if i < indexNS:
                cutBefore += sb[i]

        cutAfter = ""
        just2 = "" 
        for i  in range(ns):
            if i>indexNS :
                cutAfter += sb[i]

        for i in range(decimals):
            just2 += cutAfter[i]
        real = f"{cutBefore}.{just2}"
        print(real)
    else:
        print(n)

n = int(input("enter number : "))
sumx = 0
for i in range(n):
    q = float(input(f"enter quility life {i+1} : "))
    y = int(input(f"enter year {i+1} : "))
    if (q > 0 and q <= 1) and (y > 0 and y <= 100):
        sumx += q * y
    else:
        print("dead")
        break

check(sumx, 3)

