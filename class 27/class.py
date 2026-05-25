class bankAcount:
    def __init__(self,holder_name,account_number,balace):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balace = balace
    def deposit(self):
        while True:
            depositamount = int(input("Enter the number that you want to deposit to the account: "))
            self.balace += depositamount
            print (f"{depositamount} has been succefully added to the account.")
            break
    def withdraw(self):
        while True:
            withdrawamount = input("how much do you want to withdraw from the account: ")
            if withdrawamount <= self.balance:
                self.balance -= withdrawamount
                print(f"{withdrawamount} has been succefully withdrawn from the account.")
                break
            else:
                print ("Insuffcient funds.")
                continue








account1 = bankAcount("ben",1,0)
account2 = bankAcount("jeff",2,0)

account1.deposit()