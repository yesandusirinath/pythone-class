class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Object car called {brand} was created.")

    def drive(self):
        print(f"{self.brand} is driving.")
    def brake(self):
        print (f"{self.brand} has braked.")

ford = Car("Ford","Mustang",1965)
honda = Car("Honda","Civic",2022)

ford.drive()
honda.brake()