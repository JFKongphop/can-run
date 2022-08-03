# Greetings!
def duplicateMid():
    word = str(input("enter word : "))
    firstPart = word[0 : len(word) - 1]
    midPart = word[1 : len(word) - 1]
    lastPart = word[len(word) - 1]
    newDuplicate = firstPart + (midPart * 1) + lastPart
    print(firstPart)
    print(midPart)
    print(lastPart)
    print(newDuplicate)
        
