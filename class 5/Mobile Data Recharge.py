print("Mobile Data Recharge")
data_usage = int(input("How many data did you use in GB: "))
prime_user = input("Do you have primium: ")
per_GB = 300
discount = 0             #keep track of all the numbers
price = 0
if data_usage > 5 :
    price = price + 50                      #add 50 if it is more than 5GB
GB = data_usage * per_GB
total = GB + price                      #calculate the total
 
if prime_user == "yes":
    discount = total * 0.1                     #ckeck if you have primium
else :
    print("prmium is not activated")    
final_price = total - discount                #calucalate the final price
print(f""" 
==================================Bill==================================
 
      Data used                              {data_usage}GB
      price per GB                           {per_GB}
      Do you have primium                    {prime_user}
      If you have primium 10%                {discount}
      
      Total                                  {final_price}

========================================================================
""")     #print the final bill