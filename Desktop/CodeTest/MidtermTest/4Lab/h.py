def tedDoll():
    tedPrice = int(input("enter ted price : "))
    dollPrice = int(input("enter doll price : "))
    budget = int(input("enter budget : "))
    
    amountTed = budget // tedPrice # amount ted
    totalTedPrice = amountTed * tedPrice # total price of ted

    boughtTed = budget - totalTedPrice # balance after buy ted
    
    amountDoll = boughtTed // dollPrice # amount doll
    totalDollPrice = amountDoll * dollPrice # total price of doll
    if totalTedPrice + totalDollPrice == budget: print(f"Teddy : {amountTed} |  Doll : {amountDoll}")
    else : print("not possilble")

tedDoll()
