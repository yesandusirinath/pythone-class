# ## **Assignment 1 — Supermarket Discount**

# Write a program that takes:

# - total purchase amount
# - coupon code (“SAVE10”)

# Rules:

# - If amount > 500 → 5% discount
# - If coupon code is correct → additional ₹50 off
# - Print final bill.


purchaseAmount = int(input("Enter your purchase price: "))
couponFromUser = input("Enter coupon code: ").upper()

VALID_COUPON = "NEWYEAR20"
discountFor500 = 0
coupinDiscount = 0
if purchaseAmount >500:
    discountFor500 = purchaseAmount * (5/100)
if couponFromUser == VALID_COUPON:
     coupinDiscount = 50

discountedPrice = purchaseAmount -discountFor500 - coupinDiscount

print(f"""  
    ==============================================================
      dis pr : {discountedPrice,coupinDiscount,discountFor500}

 """)




