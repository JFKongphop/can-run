def fibonucci(n):
    print(n)
    a = fibonucci(n-2) + fibonucci(n-1)
    print(a) 
fibonucci(5)