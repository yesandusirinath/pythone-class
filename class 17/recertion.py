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
i = 2
sum = 0


print("THE FUNCTION")
def g():
    global n
    if n == 0:
        return
    print(n)
    n -= 1
    g()


g()