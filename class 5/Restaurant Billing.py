#Inputs:

#- food total
#- service charge % (5 or 10)
#- membership (yes/no)

#Rules:

#- Add service charge
#- If membership yes → 5% discount on final bill
#- Print detailed bill using f-string.
print("Restaurant Billing")
total_price = int(input("What is the total price of your food: "))
membership = input("Do you have a membership: ")
price = total_price
discount = 0
if membership == "yes":
    discount = price*0.05
else :
    print("No discout for the membership")
charge = price*0.1
total = price - discount
final_price = total + charge
print(f""" 
=================================Bill=================================
      
      The price of you food                          £{total_price}
      Discount from the membership is 5%
      Do you have a membership                        {membership}
      The service charge                             £{charge}
      
      The total                                       {final_price}

======================================================================
""")
    




