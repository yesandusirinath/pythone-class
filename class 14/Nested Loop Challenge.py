n = int(input("Enetr a number: "))
upto = int (input ("Up to what number do you need the multiplication table to: "))
print (f"Multiplication Table of {n}")
f = 1
while upto+1>f:
    a = n * f 
    print (f"{n} x {f} = {a}")
    f += 1