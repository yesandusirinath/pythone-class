class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        print(f"object animal called {name} is created.")

    def makeSound (self):
        print (f"The {self.name} makes {self.sound}.")

cat = Animal("Cat","meows")
dog = Animal("Dog","barks")

cat.makeSound()
