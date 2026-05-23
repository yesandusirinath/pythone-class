class Student:
    def __init__(self,name,rollNumber,mathmarks,Biomarks,csmarks,englishmarks):
        self.name = name
        self.rollNumbers = rollNumber
        self.mathmarks = mathmarks
        self.Biomarks = Biomarks
        self.csmarks = csmarks
        self.englishmarks = englishmarks
        print (f"A student called {name} was created.")
        print("")
    def personal_student_detail(self,total_percentage):
            print(f"Name: {self.name}")
            print(f"RollNumber: {self.rollNumber}")
            print(f"Marks: {total_percentage}")

    def getGrade(self):    
        total = self.mathmarks + self.csmarks + self.Biomarks + self.englishmarks
        total_percentage = (total/400) * 100
        self.personal_student_detail(total_percentage)
        if total_percentage >= 90:
            print("Got a grade A")
        elif total_percentage >= 80:
            print("Got a grade B")
        elif total_percentage >= 70:
            print("Got a grade C")
        else:
            print("Got a grade D")

Yesandu = Student("Yesandu",69,70.5,50,60,70)
Akash = Student("Akash",89,90.5,50,40,90)
Chavin = Student("Chavin",79,80,30,60,50)

Yesandu.getGrade()