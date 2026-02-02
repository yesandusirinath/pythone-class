n = int(input("Enter a number: "))
IsNPrime = True
for i in range(2,n):
    rem = n % i
    if rem == 0:
        IsNPrime = False
if IsNPrime == True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")    

