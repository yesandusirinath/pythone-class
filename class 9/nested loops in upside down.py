n = int(input("Enter a number: "))

for i in range (1,n+1):
    for y in range (n-i+1):
        print ("*",end="  ")
    print (end="\n")    