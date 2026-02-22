def sub(n1,n2):
    print(f"subtraction of {n2} from {n1} is {n1 - n2} ")
def mul(n1,n2):
    print(f"Multiplication of {n1} and {n2} is {n1*n2}")
def div(n1,n2):
    print (f"{n1} diveded by {n2} is {n1/n2}")
def add(n1,n2):
    print (f"addition of {n1} and {n2} is {n1+n2}")

while True:
    print(f""" 
================calculator================
          
  1. Addition
  2. Subtarction
  3. Multiplication
  4. division
  5. stop    
==========================================
""")
    choice = (input("Eneter your choice (1/2/3/4/5): "))
    n1 = int (input("Enetre a number: "))
    n2 = int (input("Eneter a number: "))
    if choice == "1":
        add(n1,n2)
    elif choice == "2":
        sub(n1,n2)
    elif choice == "3":
        mul(n1,n2)
    elif choice == "4":
        div(n1,n2)
    elif choice == "5":
        break
    else :
        print("invalid")
