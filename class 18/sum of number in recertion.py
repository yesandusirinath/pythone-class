

i = 2
sum = 0

def f ():
    global i
    global sum
    if i == 0:
        return
    sum += i
    i -= 1
    f()
f()    
print (sum)


#def f1(n):
#    if n == 0 :
#       return 0
#    return n + f1(n-1)
#print(f1(3))


#def f1(n):
#    if n == 1 :
#        return 1
#    return n * f1(n-1) 
#print(f1(3))




#def f1(n):
#    if n == 0:
#        return
    

#print(f1(43))