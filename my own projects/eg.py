#i = 0
#def f():
#    global i
#    if i == 11:
#        return
#    print(i)
#    i +=1
#    f()
#f()
i =  int (input("Enter a number: "))
f = i
n = i
print ("FOR i IN RANGE")
for i in range (i,0,-1):
   print(i)

print("WHLE LOOP")
f +=1
while f>1:
    f -= 1
    print (f)

print("THE FUNCTION")
def g():
    global n
    if n == 0:
        return
    print(n)
    n -= 1
    g()


g()
