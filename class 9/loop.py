The_sum = 0
number = int(input("Enter a number: "))
for i in range (1,number+1):
    remader = i%2
    if remader == 0:
        The_sum += i
        print("is a even number:",i)
        
print(f"The sum of those number are {The_sum}")
