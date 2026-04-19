print ("Expenses traker")

QUwarning = True
expensesList = []

def addexpenses():
    while True:
        print ("Go back to the menu type back to the menu. ")
        print ("Go back to the last quation type back. ")
        catergory = input("What is the catergory that your expense is?: ")
        if catergory.strip().lower() == "back to the menu" or catergory.strip().lower() == "back":
            break
        else:
            while True:
                amount = input(f"What is the amount that you spend on {catergory}: ")
                if amount.strip().lower() == "back":
                    break
                elif amount.strip().lower() == "back to the menu":
                    break
                elif any(item["catergory"] == catergory and item["amount"] == amount for item in expensesList):
                    print ("This is already in the list.")
                    break
                elif amount.isdigit():
                    while True:
                        global QUwarning
                        if QUwarning == False:
                            print ("You are getting this messege because you got rid of the warning question")
                            print ("To get it back type warning")
                        asknote = input ("Do you want to add any note: ")
                        if asknote.strip().lower() == "warning":
                            if QUwarning == False:
                                print ("The warning question will be asked again.")
                                QUwarning = True
                                continue
                            else:
                                print ("The warning question is already there.")
                                continue
                        elif asknote.strip().lower() == "yes":
                            note = input("What is the note that you want to add: ")
                            if note.strip().lower() == "back":
                                continue
                            elif note.strip().lower() == "back to the menu":
                                break
                            else:
                                expense = {
                                    "catergory": catergory,
                                    "amount"   : amount,
                                    "notes"    : note}
                                expensesList.append(expense)
                                print ("Added to the list.")
                                break                         
                        elif asknote.strip().lower() == "no":                            
                            print ("Note was not add to the expense.")                   
                            while True:                                                 
                                if QUwarning == True:                                    
                                    print ("If you want get rid of this question type don't ask again.")           
                                    warning = input("Do you want to go back: ")                                    
                                    if warning.strip().lower() == "yes":
                                        break
                                    elif warning.strip().lower() == "no":
                                        note = "-"
                                        expense = {
                                        "catergory": catergory,
                                        "amount"   : amount,
                                        "notes"    : note}
                                        expensesList.append(expense)
                                        print ("Added to the list.")         
                                        break
                                    elif warning.strip().lower() == "don't ask again":
                                        QUwarning = False
                                        break
                                    elif warning.strip().lower() == "back to the menu":
                                        return
                                    else:
                                        print("The only answser are yes and no.")
                                        continue       
                                else:
                                    note = "-"
                                    expense = {
                                    "catergory": catergory,
                                    "amount"   : amount,
                                    "notes"    : note}
                                    expensesList.append(expense)
                                    print ("Added to the list.")
                                    break             
                            if warning.strip().lower() == "yes":
                                continue
                            elif warning.strip().lower() == "no":
                                break
                        elif asknote.strip().lower() == "back":
                            break
                        elif asknote.strip().lower() == "back to the menu":
                            return
                        else:
                            if QUwarning == True:
                                print ("Only option available are yes and no.")
                            elif QUwarning == False:
                                print ("Only option available are warning and yes and no.")
                    if asknote.strip().lower() == "back":
                        continue
                    elif note.strip().lower() == "back to the menu":
                        return
                    elif note:
                        break
                else:
                    print ("You can only enter numbers.")
                    continue
            if amount.strip().lower() == "back to the menu":
                break
            elif amount.strip().lower() == "back":
                continue
            elif any(item["catergory"] == catergory and item["amount"] == amount for item in expensesList):
                continue
def changelist ():
    if expensesList:
        while True:
            print ("Go back to the menu type back to the menu.")
            print ("Go back to the last question type back.")
            catergorytype = input("What is the name of the category that you want to change: ")
            if catergorytype.strip().lower() == "back" or catergorytype.strip().lower() == "back to the menu":
                return
            elif catergorytype.strip().lower() == "category":            
                matches = []
                while True:
                    whatCategory = input("what is the name of the category: ")
                    if any(item["catergory"].strip().lower() == whatCategory for item in expensesList):
                        for item in expensesList:
                            if item ["catergory"].strip().lower() == whatCategory:
                                matches.append(item)
                        if len(matches) == 1:
                            newCategory = input(f"What do you want to change {whatCategory} to: ")
                            matches[0]["catergory"] = newCategory
                            break
                        else:
                            print("Which one do you want to change?")
                            for i in range(len(matches)):
                                print("Choice", i + 1)
                                print("Catergory:", matches[i]["catergory"])
                                print("Amount:", matches[i]["amount"])
                                print("Notes:", matches[i]["notes"])
                                print()
                            while True:
                                choice = input("Type the number: ")
                                if choice.strip().lower() == "back":
                                    break
                                elif choice.strip().lower() == "back to the menu":
                                    return
                                elif choice.isdigit():
                                    newCategory = input("What is the new category?: ")
                                    matches[int(choice) - 1]["catergory"] = newCategory
                                    print ("Succefully chenged")        
                                    break
                                else:
                                    print ("you can only enter a number")
                                    continue
                    if whatCategory.strip().lower() == "back":
                        break
                    elif whatCategory.strip().lower() == "back to the menu":
                        return
                    elif newCategory:
                        break
                    else:
                        print (f"{whatCategory} is not in the list.")
                        continue
            elif catergorytype.strip().lower() == "amount":
                matches = []
                while True:
                    whatamount = input("what is the amount: ")
                    if any(item["amount"].strip().lower() == whatamount for item in expensesList):
                        for item in expensesList:
                            if item ["amount"].strip().lower() == whatamount:
                                matches.append(item)
                        if len(matches) == 1:
                            newamount = input(f"What do you want to change {whatamount} to: ")
                            matches[0]["amount"] = newamount
                            break
                        else:
                            print("Which one do you want to change?")
                            for i in range(len(matches)):
                                print("Amount:", matches[i]["amount"])
                                print("Category:", matches[i]["catergory"])
                                print("Notes:", matches[i]["notes"])
                                print()
                            while True:
                                choice = input("Type the number: ")
                                if choice.strip().lower() == "back":
                                    break
                                elif choice.strip().lower() == "back to the menu":
                                    return
                                elif choice.isdigit():
                                    newamount = input("What is the new amount?: ")
                                    matches[int(choice) - 1]["amount"] = newamount
                                    print ("Succefully chenged")        
                                    break
                                else:
                                    print ("you can only enter a number")
                                    continue
                    if whatamount.strip().lower() == "back":
                        break
                    elif whatamount.strip().lower() == "back to the menu":
                        return
                    elif newamount:
                        break
                    else:
                        print (f"{whatamount} is not in the list.")
                        continue
            elif catergorytype.strip().lower() == "note" or catergorytype.strip().lower() == "notes":
                matches = []
                while True:
                    whatnote = input("what is the note: ")
                    if any(item["note"].strip().lower() == whatnote for item in expensesList):
                        for item in expensesList:
                            if item ["note"].strip().lower() == whatnote:
                                matches.append(item)
                        if len(matches) == 1:
                            newnote = input(f"What do you want to change {whatamount} to: ")
                            matches[0]["note"] = newnote
                            break
                        else:
                            print("Which one do you want to change?")
                            for i in range(len(matches)):
                                print("Notes:", matches[i]["notes"])                                
                                print("Catergory:", matches[i]["catergory"])
                                print("Amount:", matches[i]["amount"])
                                print()
                            while True:
                                choice = input("Type the number: ")
                                if choice.strip().lower() == "back":
                                    break
                                elif choice.strip().lower() == "back to the menu":
                                    return
                                elif choice.isdigit():
                                    newnote = input("What is the new note?: ")
                                    matches[int(choice) - 1]["note"] = newnote
                                    print ("Succefully chenged")    
                                    break
                                else:
                                    print ("you can only enter a number")
                                    continue
                    if whatamount.strip().lower() == "back":
                        break
                    elif whatamount.strip().lower() == "back to the menu":
                        return
                    elif newnote:
                        break
                    else:
                        print (f"{whatamount} is not in the list.")
                        continue
    else:                
        print ("There is nothing on the list.")
        return
def showlist ():
    if expensesList:
        for item in expensesList:
            print("Catergory:", item["catergory"])
            print("Amount:", item["amount"])
            print("Notes:", item["notes"])
            print()
    else:
        print("There is nothing on the list.")
        return        


while True:
    print ("""
    ------------------------Traker------------------------

            1. Add an expenses
            2. Change any expenses.
            3. Remove any expenses.
            4. Sum of all the expenses.
            5. See just one catergory
            6. All of the expense with the amount and notes.
            7. See it as a bill. 
            8. Exit 

    ------------------------------------------------------
    """)
    choice = input("Enter the number of your choice: ")
    if choice.strip() == "1":
        addexpenses()
    elif choice.strip() == "2":
        changelist()
    elif choice.strip() == "3":
        pass
    elif choice.strip() == "4":
        pass
    elif choice.strip() == "5":
        pass
    elif choice.strip() == "6":
        showlist()
    elif choice.strip() == "7":
        pass
    elif choice.strip() == "8":
        break
    else:
        print ("The only option are the number on the left side of the choices.")
        continue