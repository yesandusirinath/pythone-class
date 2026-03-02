import math

def radians (n1):
    print (f"The radian is {n1* math.pi/180}")
n1 = int (input("Eneter a number: "))
radians (n1)


def add (*arg):
    sum = 0
    for x in arg:
        sum+=x
    print (f"sum : {sum}")
add(1,1,2,3,4,5,6,6,6,6666,7)