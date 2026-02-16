n= int(input ("Enter a number: "))
oreginalNum=n
reversedDigit = 0
while 0< n:
    remaider = n %10
    reversedDigit = reversedDigit*10 + remaider
    n = n//10
if oreginalNum == reversedDigit:
    print (f"{oreginalNum} is a palidrome number")
else:
    print(f"{oreginalNum} is not a palidrom number")
print (reversedDigit)

