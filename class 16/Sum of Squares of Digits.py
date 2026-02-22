n = int(input("Enter a number: "))
f= n
sum = 0
while n>0 :
    dig = n%10
    sum += dig**2
    n = n//10
print (f" Sum of Squares of {f} is {sum}")