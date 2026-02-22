n = int(input("Enter a number: "))
f= n
sum = 0
while n>0 :
    dig = n%10
    print (f"dig is {dig}")
    sum += dig**2
    print (f"the sum is {sum}")
    n = n//10
    print (f"n is {n}")
print (f" Sum of Squares of {f} is {sum}")
