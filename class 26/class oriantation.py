class Human:
    #1. constructor: soul 2. properties (variables) 3. functinalities (functions)
    
    # 1. contructor
    def __init__(self,name,age,weight,height):
        # properties varibles
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        print (f"One object of Human class called {name} is created at {self}")
        print ("")

    #behavior 
    def walk (self):
        print (f"Human is walking")
    def eat (self):    
        print (f"{self.name} is eating")

# objects / real instances / real Human can be created
alif = Human("alif Azhar",13,40,175)
yesandu = Human("Yesandu Sirinath",12,41,176)

print (alif.name)
print (yesandu.name)
alif.eat()
yesandu.eat()