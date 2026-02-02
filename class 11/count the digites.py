n = int(input ("Enter a number: "))
numOfDigits = 0
f=n

while n>0:
    numOfDigits +=1
    n = n//10
print (f"There are {numOfDigits} in the number {f} ")    
