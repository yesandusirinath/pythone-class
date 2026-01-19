n = int(input("Enter a number: "))

for i in range (1,n+1):
    x=0
    for y in range (i):
        x += 1 
        print(x,end=" ")
    
    print(end="\n")     