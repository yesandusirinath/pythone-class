n = int(input("Eneter a number: "))
sum = 0
while n>0:
    dig = n %10
    sum += dig**2
    n = n//10
print (sum)