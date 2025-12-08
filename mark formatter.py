print("makeing a student card")
name = input("What is your name: ")
className = input("what is your class:")
maths = int(input("Enter the mark for the maths subject: "))
iCT = int(input("Enetr the mark for the ICT subject: "))
bio = int(input("Enetr the mark for the Bio subject: "))
avarage = (maths + iCT + bio) /3
print(f"Student name is: {name} \n Student class is: {className} \n the marks for maths: {maths} \n the marks for maths: {iCT} \n the marks for maths: {bio} \n the average mark is {avarage} ")

