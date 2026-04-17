print ("money tracker")

moneylist = {}


def addexpenses ():
    while True:
        print ("Back to the menu type back to the menu")
        print ("Back to the last quation and change the anwser type back")
        
        catergory = input("What catergory or the name of the itme that you spend on: ")
        
        if catergory.lower() == "back to the menu" or catergory.lower() == "back" :
            break
        
        else:
            while True:
                amount = input("Enter the amount that you spend on it: ")

                if amount.lower() == "back":
                    break
            
                elif amount.lower() == "back to the menu":
                    break
                
                elif not amount.isdigit():
                    print ("You only can enter a numbers")
                    continue
                
                else:
                    while True:
                        asknote = input("Do you want to add any note to that:(yes/No) ")

                        if asknote == "yes":

                            note = input("what is the note that you want to add to it: ")
                    
                            if note == "back":
                                continue
                            else:
                                break
                            
                        elif asknote.lower() == "back":
                            break

                        elif asknote.lower() == "back to the menu":
                            break
                    
                        elif asknote == "no":
                            print ("A note was not added to the expenses list.")
                    
                            wantToGoBack = False
                    
                            while True:
                                backToTop = input("Do you want to go back(Yes/No): ").lower()
                        
                                if backToTop == "yes":
                                    wantToGoBack = True
                                    break
                        
                                elif backToTop == "no":
                                    break
                        
                                else:
                                    print ("The only option are yes and no.")
                    
                            if wantToGoBack == True:
                                continue
                    
                            elif wantToGoBack == False:
                                break        

                            else:
                                print ("The only option are yes and no.")
                        else:
                            break
            if amount.lower() == "back":
                continue
            elif amount.lower() == "back to the menu":
                break
        list1=[catergory, amount, note]    
        addToList (list1)


print ("""
---------------------Menu---------------------
       
       1. Add something to the expenses.
       2. Change any expenses.
       3. Remove any expenses.
       4. Sum of all the expenses.
       5. The name of all the expenses.
       6. All of the expenses with the amonte and any notes that you added to it.
       7. Exit

----------------------------------------------
""")

def addToList (list2):
    moneylist.append(list2)
    print ("Money list :",moneylist)





option = input("Enter your choice: ")
if option == "1" :
    addexpenses()
