n = int(input("Eneter a number: "))
f=n
even = []
odd = []
while n>0 :
    dig = n%10           
    remai = dig%2
    if remai == 0 :
        even.append(dig)
    else:
        odd.append(dig)
    n = n//10
print(f"""
    The number is = {f}
    The odd numbers = {odd}
    The even numbers = {even}

""")