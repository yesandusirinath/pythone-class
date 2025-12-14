print("Supermarket dicount")
print("You can ues Dollers, Pounds and Euros")     #say what is happening in this programe
while True:
    currency = input("What currency do you use: ").lower() #ask what currency do you have
    symbols = {"doller": "$",  #check the currency
           "dollers": "$",
           "pounds": "£",
           "pound": "£",         #have all of the currency so that if you says singular and plural it still works
           "euros": "€",
           "euro": "€"}
    if currency in symbols:              #tells what currency you are using in this programe
        symbol = symbols[currency]
        print(f"Currency is accepted:{symbol}")  #tell you what currncey is use in this bill
        print(f"You currency is {currency}")
        break
    else:
        print("This currency is not supported. Please try again.\n")   #comes here if you gives the wroge currency
StartPrice = int(input("What is the price of the product: "))  #ask for the price of the product
price = StartPrice        #keeps the first price of the product so that it can be used in the bill
discount = 0   # keeps all of the changes 
tries = 0
MaxTries = 3       # tell how many tries do you have
couponDiscount = 0
discountFromTheCoupon = 0
if price >500: # checks if the prise if over or under 500 
    discount = price * 0.05
while tries < MaxTries:
    coupon = input("Do you have coupon: ").lower()    #ask you that do you have a coupon
    if coupon == "no":
        print("No coupon has been applied")  #is said no tell to programe that to coupon is being applied
        break
    elif coupon == "yes":
        code = input("Enter your coupon code: ")   #goes here only if you said yes that you do have coupon
        tries += 1    #add one try to the tries so that you can't keep trying forever
        if code == "SAVE10":     #check is the coupon code is correct
            print("Coupon is accepted!")     #tell you what happed to your coupon code
            discountFromTheCoupon = discountFromTheCoupon + 10  #keep track of how much discount to get from coupons
            price = price - 10    #change the price to the new price
            couponDiscount = couponDiscount + 2
            break
        else:
            if tries < MaxTries:        #only comes here if you got the coupon code wroge
                print("The coupon code is incorrect")
                retry = input("Do you want to try again: ").lower()
                if retry == "no":
                    print("No coupon has been applied")   #ask you that do you want to try agian
                    break
            else:
                print("Too many attempts. No coupon has been applied")     #if you eneter the wroge coupon code for 3 times it canceles it and move with out it           
                couponDiscount = couponDiscount + 1
final_price = price - discount       #calculate the final price
import datetime                       #check the date and time of the present moment to be used on the bill
now = datetime.datetime.now()
if couponDiscount == 0:         
    DidTheCouponActivate = "no"
elif couponDiscount == 1:
    DidTheCouponActivate = "Failed to apply"   # to check if the coupon has activated 
elif couponDiscount == 2:                #And to keep track of what happend to the coupon
    DidTheCouponActivate = "yes"        
print(f"""
------------------------------Bill------------------------------
Date:{now.strftime("%d/%m/%y")}                           Time: {now.strftime("%H:%M")}

      
The price is                                  {symbol}{StartPrice}
The discount                                  {symbol}{discount}
Do you have a coupon                          {DidTheCouponActivate}
Discount from the coupon                      {symbol}{discountFromTheCoupon}

The total                                     {symbol}{final_price}

-----------------------------------------------------------------
""")                #print the bill for you to see what happen and to tell you the final price