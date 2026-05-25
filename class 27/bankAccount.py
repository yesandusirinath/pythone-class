balance = 0
def deposit():
    while True:
        depositamount = input("Enter the number that you want to deposit to the account: ")
        if depositamount.strip() == int:
            balance += depositamount
            print (f"{depositamount} has been succefully added to the account.")
            break
        else:
            print("You can only enter numbers.")
            continue
def withdraw():
    while True:
        withdrawamount = input("how much do you want to withdraw from the account: ")
        if withdrawamount.strip() == int:
            if withdrawamount <= balance:
                balance -= withdrawamount
                print(f"{withdrawamount} has been succefully withdrawn from the account.")
                break
            else:
                print ("Insuffcient funds.")
                continue
        else:
            print ("you can only enter numbers")
            continue
def show():
    print (f"the current balance is {balance}.")





while True:
    print("""
---------------------Bank Account---------------------
        
        1. Deposit money
        2. Withdraw money
        3. Send
        4. Receive
        5. Display account details
        6. Exit

------------------------------------------------------
""")
    choice = input("Enter the number for the option you want to pick: ")
    if choice.strip() == "1":
        deposit()
    elif choice.strip() == "2":
        withdraw()
    elif choice.strip() == "3":
        show()
    else:
        print ("Invaild choice pick a number from the number displayed above.")
        continue
