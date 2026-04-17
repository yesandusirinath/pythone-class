print ("Monthly expenses")

moneylist = []

def addexpenses():
    while True:
        print ("Back to the menu type back to the menu.")
        print ("Back to the last quation and change the anwser to the last quation type back.")
        catergory = input("What catergory or the name of the itme that that you spend on: ")
        if catergory.lower() == "back to the menu" or catergory.lower() == "back" :
            break
        else:
            while True:
                amount = input("Enter the amount that you spend on it: ")
                if amount.lower() == "back":
                    break

some = input("Something")
if some == "1":
    addexpenses()