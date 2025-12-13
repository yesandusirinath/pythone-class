# ### **Activity 1— Online Shopping Discount System**

# Input:

# - price
# - membership (yes/no)

# If price > 1000 → 10% discount

# If member → additional 5%

# Else → no discount
price = int(input("What is the price: "))
membership = input("Do you have the mebership: ")
if membership == "yes":
    price = price - (price*0.05)
if price > 1000:
    price = price - (price*0.1)
print(f"The price is: {price}")
