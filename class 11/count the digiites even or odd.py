n = int(input("Enetre a number: "))
even = 0
odd= 0
evens = []
odds = []
while n >0 :
    dig = n%10
    remaider = dig%2
    if remaider == 0:
        even += 1
        evens.append(dig)
    else :
        odd +=1  
        odds.append(dig)

    n = n//10
print (f"The number od even number {even} and There are {odd} odd number. evens {evens}, odds : {odds}")    
