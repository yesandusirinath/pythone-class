#def f1 (*args):
#    sum = 0
#    for x in args:
#        sum+= x
#    print (f"The sum is {sum}")

#f1(10,20,30)


# def f1 (**args):
#     for key,value in args.items ():
#         print(f"key : {key} . value {value}")

#f1 (a=1,b=2,c=3,d=4,e=5)

numbers = [5,4,3,7,8]


def f1 (numbers):
    return numbers **2

def f2 (num):
    rem = num % 2
    if rem == 0:
        return True
    else:
        return False
for x in range(5):
    if f2(numbers[x]) == True:
        print(numbers[x])
        


for i in range(5):
    print (f" The square of {numbers[i]} is {f1(numbers[i])}")