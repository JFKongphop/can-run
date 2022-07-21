team = int(input("enter number of team : "))
timeThrow = int(input("enter number of throwv : "))
valueThrow = 0
va1 = 0
va2 = 0
va3 = 0
va4 = 0
for i in range(team):
    for j in range(timeThrow):
        if i == 0:
            valueThrow = int(input(f"Throw from team {i+1} time {j+1} to throw : "))
            if valueThrow > va1:
                va1 = valueThrow
            valueThrow = 0
        elif i == 1:
            valueThrow = int(input(f"Throw from team {i+1} time {j+1} to throw : "))
            if valueThrow > va1:
                va2 = valueThrow
            valueThrow = 0
        elif i == 2:
            valueThrow = int(input(f"Throw from team {i+1} time {j+1} to throw : "))
            if valueThrow > va1:
                va2 = valueThrow
            valueThrow = 0
        elif i == 3:
            valueThrow = int(input(f"Throw from team {i+1} time {j+1} to throw : "))
            if valueThrow > va1:
                va2 = valueThrow
            valueThrow = 0
        
# valueThrow = 0
# for i in range(team):
#     if 

# use to get all such as 4 team and 3 throw that all is 12 all sort or find the highest and find of index in their variable for show of the range when are show in somem team 
# a = 10,20,30
# print(type(a[1]))

        

# maxn = 0
# for i in range(4):
#     n = int(input(f"enter number {i+1} : "))
#     if(n > maxn):
#         maxn = n
# print(n)
