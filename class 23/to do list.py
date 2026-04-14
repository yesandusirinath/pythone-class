doList = []

import json
import os 

folder = "data"

filename =  os.path.join(folder, "doList")

os.makedirs(folder, exist_ok=True)

if os.path.exists(filename):
    with open(filename, "r") as f:
        doList = json.load(f)

else:
    doList = []

print("current list: ", doList)


def addtask ():
    print ("When you need to stop type stop")
    while True:
        task = input("give the thing that you need on the list: ")
        if task in doList:
            print("This Task already in the list")
        elif task == "stop":
            break
        else:
            doList.append (task)
            print (f"succesfully added {task} to the list.")

def removetask ():
    print ("When you need to stop type stop")
    while True:
        item = input("Give the name of the task that you need to remove: ")
        if item in doList:
            doList.remove(item)
            print(f"The {item} task has succesfully been removed.")
        elif item == "stop":
            break
        else:
            print ("this task is not in the list.")

def ShowTheList ():
    print (doList)

def indexNumber ():
    print ("If you want to go back to the menu type back.")
    character = input ("Give the name of the task that you need to find the index number in: ")
    if character in doList :
        print (f"The index number of the task {character}is {doList.count(character)}.")
    elif character == "back":
        return
    else :
        print ("this task is not in the list")

def changetask ():
    print ("if you want to go back to the menu type back.")
    TaksName = input("Give the task name that you need to change: ")
    if TaksName in doList:
        update = str (input(f"what do you want to change the {TaksName} into: "))
        doList[TaksName] = update
        print (f"The {TaksName} task it succesfully change into {update}")
    elif TaksName == "back":
        return
    else:
        print (f"The task {TaksName} is not the list ")

def removeall ():
    doList.clear()

while True :
    print (""" 
----------------Menu----------------
           
        1. Add Task
        2. Remove task
        3. Remove all tasks at once
        4. Show All The Tasks
        5. Show the index number of that task
        6. Change a task 
        7. Exit
           
------------------------------------
            """)
    chioce = input("Give the number of your chioce: ")
    if chioce == "1":
        addtask()
    elif chioce == "2":
        removetask()
    elif chioce == "3":
        removeall()
    elif chioce == "4":
        ShowTheList()
    elif chioce == "5":
        indexNumber()
    elif chioce == "6":
        changetask()
    elif chioce == "7":
        print ("Thank you for your time")
        with open(filename, "w") as f:
            json.dump(doList, f)
        print("Updated list saved!")
        break
    elif chioce == "done" :
        break
    else:
        print ("This is not one of the chioces of numbers in the menu. Those number are to the left side from the options")