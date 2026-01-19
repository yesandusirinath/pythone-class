n = int(input("Enetre a number: "))
y = n
for i in range (1,n+1):
    y -=1
    j = 0
    for x in range (y+1):
        j +=1
        print (j,end = "  ")
    print(end="\n")