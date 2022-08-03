n = int(input("number : "))
senList = []
for i in range(n):
    sentence = str(input(f"sentence {i + 1} : "))
    if "Simon says" in  sentence:
        new = sentence.replace("Simon says", "")
        senList.append(new)

for i in senList:
    print(i)
