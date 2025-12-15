print("===============currency converter============================")

# in srilankan valuye
# currencyMap = {
#     "dollor": 309,
#     "pounds": 413
# }

cuurencyYouWantToConvert = (input("Enter cuurrr:  "))

if cuurencyYouWantToConvert == "dollor":

        dollarAmount = float(input("Enter amount in dollar: "))
        srilankanAmount = dollarAmount * 309
        print(f"{dollarAmount} : {srilankanAmount} rupees")
if cuurencyYouWantToConvert == "pounds":

        pAmount = float(input("Enter amount in dollar: "))
        srilankanAmount = pAmount * 413
        print(f"{pAmount} : {srilankanAmount} rupees")
