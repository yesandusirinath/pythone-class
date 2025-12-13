print("makeing a student card")
name = input("What is your name: ")
className = input("what is your class:")
age = input("How old are you: ")
print("Enter the are that you got out of 100 only")
firstSubject = input("Name an subject that you have: ")
secondeSubject = input("Name an different subject that you have: ")
thirdSubject = input("Name an another subject that you have: ")
fourthSubject = input("Name an another subject that you have: ")
fifthSubject = input("Name an another subject that you have: ")
SubjectA = int(input(f"Enter the mark for the {firstSubject} subject: "))
SubjectB = int(input(f"Enetr the mark for the {secondeSubject} subject: "))
SubjectC = int(input(f"Enetr the mark for the {thirdSubject} subject: "))
SubjectD = int(input(f"Enetr the mark for the {fourthSubject} subject: "))
SubjectE = int(input(f"Enetr the mark for the {fifthSubject} subject: "))
avarage = (SubjectA + SubjectB + SubjectC + SubjectD + SubjectE) /5
percentage = ((SubjectA + SubjectB + SubjectC + SubjectD + SubjectE) / 500) * 100
total = SubjectA + SubjectB + SubjectC + SubjectD + SubjectE
print(f""" 
--------------------------------------Report card--------------------------------------
      
The student's name is: {name}
The class is: {className}
The students age is: {age}

The student does {firstSubject} {secondeSubject} {thirdSubject} {thirdSubject} {fourthSubject} {fifthSubject}

The mark for {firstSubject} is: {SubjectA}
The mark for {secondeSubject} is: {SubjectB}
The mark for {thirdSubject} is: {SubjectC}
The mark for {fourthSubject} is: {SubjectD}
The mark for {fifthSubject} is: {SubjectE}

The total mark is: {total} out of 500
The avarage mark is: {avarage}
The percentage is: {percentage}%

--------------------------------------------------------------------------------------
""")