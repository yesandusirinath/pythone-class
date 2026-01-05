print("This take all of the mounly spendings")
salery = int(input("What is you mounly salery: "))
bills = int(input("How many main bill do you have to pay mounly: "))
type_of_bill = 0
second_type_of_bill = 0
thrid_type_of_bill = 0
fourth_type_of_bill = 0
fifth_type_of_bill = 0
sixth_type_of_bill = 0
seventh_type_of_bill = 0
payment_amount = 0
second_payment_amount = 0
thrid_payment_amount = 0
fourth_payment_amount = 0
fifth_payment_amount = 0
sixth_payment_amount = 0
seventh_payment_amount = 0
while True:
    if bills == 1:
        type_of_bill = input("What is that bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        break
    elif bills == 2:
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: "))
        break
    elif bills == 3:
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        thrid_type_of_bill = input("What is the 3rd bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: "))
        thrid_type_of_bill = int(input(f"What is the amount that you pay for {thrid_type_of_bill} bill: "))
        break
    elif bills == 4:
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        thrid_type_of_bill = input("What is the 3rd bill you pay: ")
        fourth_type_of_bill = input("What is the 4th bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: ")) 
        thrid_type_of_bill = int(input(f"What is the amount that you pay for {thrid_type_of_bill} bill: "))
        fourth_payment_amount = int(input(f"What is the amount that you pay for {fourth_type_of_bill} bill: "))
        break
    elif bills == 5:
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        thrid_type_of_bill = input("What is the 3rd bill you pay: ")
        fourth_type_of_bill = input("What is the 4th bill you pay: ")
        fifth_type_of_bill = input("What is the 5th bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: "))
        thrid_type_of_bill = int(input(f"What is the amount that you pay for {thrid_type_of_bill} bill: "))
        fourth_payment_amount = int(input(f"What is the amount that you pay for {fourth_type_of_bill} bill: "))
        fifth_payment_amount = int(input(f"What is the amount that you pay for {fifth_type_of_bill} bill: "))
        break
    elif bills == 6:
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        thrid_type_of_bill = input("What is the 3rd bill you pay: ")
        fourth_type_of_bill = input("What is the 4th bill you pay: ")
        fifth_type_of_bill = input("What is the 5th bill you pay: ")
        sixth_type_of_bill = input("What is the 6th bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: "))
        thrid_type_of_bill = int(input(f"What is the amount that you pay for {thrid_type_of_bill} bill: "))
        fourth_payment_amount = int(input(f"What is the amount that you pay for {fourth_type_of_bill} bill: "))
        fifth_payment_amount = int(input(f"What is the amount that you pay for {fifth_type_of_bill} bill: "))
        sixth_payment_amount = int(input(f"What is the amount that you pay for {sixth_type_of_bill} bill: "))
        break
    elif bills == 7:   
        type_of_bill = input("What is that bill you pay: ")
        second_type_of_bill = input("What is that 2nd bill you pay: ")
        thrid_type_of_bill = input("What is the 3rd bill you pay: ")
        fourth_type_of_bill = input("What is the 4th bill you pay: ")
        fifth_type_of_bill = input("What is the 5th bill you pay: ")
        sixth_type_of_bill = input("What is the 6th bill you pay: ")
        payment_amount = int(input(f"What is the amount that you pay for {type_of_bill} bill: "))
        second_payment_amount = int(input(f"What is the amount that you pay for {second_type_of_bill} bill: "))
        thrid_type_of_bill = int(input(f"What is the amount that you pay for {thrid_type_of_bill} bill: "))
        fourth_payment_amount = int(input(f"What is the amount that you pay for {fourth_type_of_bill} bill: "))
        fifth_payment_amount = int(input(f"What is the amount that you pay for {fifth_type_of_bill} bill: "))
        sixth_payment_amount = int(input(f"What is the amount that you pay for {sixth_type_of_bill} bill: "))
        break
    if bills > 7:
        print("The maximum is 7")
    else:
        break
        

        
        
   

