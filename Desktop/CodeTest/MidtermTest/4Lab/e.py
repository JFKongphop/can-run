# not complete

def star(a, b, c = 0):
    print(" "*c+" "*(b - a)+"*"*a)
    if a > 1:
        star(a-1, b, c)
        return
    # elif b > 2:
    #     star(b-1, b-1, c+1)
    #     return
    
x = int(input())
star(x, x)
