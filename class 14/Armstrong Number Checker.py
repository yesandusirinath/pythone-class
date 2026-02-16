n= int (input("Enter a number: "))
f=n
g=n
num = 0
num2 = 0
numofdigits = 0
while g >0 :
    numofdigits +=1
    g = g// 10
while 0< n :
    remaider = n% 10
    num += remaider**numofdigits
    n = n // 10
if num == f :
    print (f"{f} is a Armstrong Number")
else :
    print (f"{f} is not a Armstrong Number")
print (num)