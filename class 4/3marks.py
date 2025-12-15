print("makeing a student card")
name = input("What is your name: ")
className = input("what is your class:")
firstSubject = input("Name a subject that you have: ")
secodeSubject = input("Name a different subject that you have: ")
thirdSubject = input("Name a another subject that you have: ")
SubjectA = int(input(f"Enter the mark for the {firstSubject} subject: "))
SubjectB = int(input(f"Enetr the mark for the {secodeSubject} subject: "))
SubjectC = int(input(f"Enetr the mark for the {thirdSubject} subject: "))
avarage = (SubjectA + SubjectB + SubjectC) /3
print(f"Student name is: {name} \n {name} class is: {className} \n the marks for {firstSubject}: {SubjectA} \n the marks for {secodeSubject}: {SubjectB} \n the marks for {thirdSubject}: {SubjectC} \n the average mark is {avarage} ")

