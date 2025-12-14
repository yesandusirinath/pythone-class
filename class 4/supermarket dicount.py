print("Supermarket dicount")
print("You can ues Dollers, Pounds and Euros")
while True:
    currency = input("What currency do you use: ").lower()
    symbols = {"doller": "$",
           "dollers": "$",
           "pounds": "£",
           "pound": "£",
           "euros": "€",
           "euro": "€"}
    if currency in symbols:
        symbol = symbols[currency]
        print(f"Currency is accepted:{symbol}")
        print(f"You currency is {currency}")
        break
    else:
        print("This currency is not supported. Please try again.\n")
StartPrice = int(input("What is the price of the product: "))
price = StartPrice
discount = 0
tries = 0
MaxTries = 3
discountFromTheCoupon = 0
if price >500:
    discount = price * 0.05
while tries < MaxTries:
    coupon = input("Do you have coupon: ").lower()
    if coupon == "no":
        print("No coupon has been applied")
        break
    elif coupon == "yes":
        code = input("Enter your coupon code: ")
        tries += 1
        discountFromTheCoupon = discountFromTheCoupon + 10
        if code == "SAVE10":
            print("Coupon is accepted!")
            price = price - 10
            break
        else:
            if tries < MaxTries:
                print("The coupon code is incorrect")
                retry = input("Do you want to try again: ").lower()
                if retry == "no":
                    print("No coupon has been applied")
                    break
            else:
                print("Too many attempts. No coupon has been applied")                
final_price = price - discount
import datetime
now = datetime.datetime.now()
print(f"""
------------------------------Bill------------------------------
Date:{now.strftime("%d/%m/%y")}                           Time: {now.strftime("%H:%M")}

      
The price is                                  {symbol}{StartPrice}
The discount                                  {symbol}{discount}
Do you have a coupon                          {coupon}
Discount from the coupon                      {symbol}{discountFromTheCoupon}

The total                                     {symbol}{final_price}

-----------------------------------------------------------------
""")                