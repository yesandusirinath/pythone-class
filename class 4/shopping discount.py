price = int(input("What is the price: "))
membershipDiscount = 0
discountOnMoreThan1000 = 0
membership = input("Do you have the mebership: ").lower()

if price > 1000:
    discountOnMoreThan1000 = (price*0.1)
if membership == "yes":
    membershipDiscount = (price*0.05)
else:
    print("Note: You did not avail any membership discount, Subscribe!!")
print(f"""
-------------------------------Bill Amount-------------------------------
      
      Product price:                              {price}     
      Membership Discount(5%):                    {membershipDiscount}
      Discount on More Than 1000(10%):            {discountOnMoreThan1000}
      Final Price:                                {price}  
                                   
-------------------------------------------------------------------------
 """)
