n = int(input ("Enter a number: "))
orgnv = n
rev = 0
while n>0:
    dig = n%10
    rev = rev*10 + dig
    n = n//10
print (f"The number is {orgnv} the reverd number is {rev}")