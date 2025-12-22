print("Movie Ticket Booking")
age = int(input("How old are you: "))
student = input("Are you a student: ")
base_ticket_price = 200           #the price of the ticket
price = base_ticket_price

if age < 12 :
    percentage = price*0.5             #what is the discount you are going to get
    price = price - percentage          # that should be 100
if student == "yes":                     
    percentage = price*0.2                 # how much dicount you get
    price = price - percentage            #this should be 40 if the age is above 12
                                          # if the is below 12 the pirce should be 20
discout = base_ticket_price - price
discount_percentage = discout / base_ticket_price *100
print(f""" 
==================================Bill==================================
      Age                                        {age}
      Is the person a student                    {student}
      The price of the ticket                    {base_ticket_price}
      The discount                               {discount_percentage}%
      Price of the discout                       {discout}
      
      The total                                  {price}

========================================================================
""")