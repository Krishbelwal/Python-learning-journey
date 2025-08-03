class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")
class Dog(Animal):
    def __init__(self, name , breed):
        Animal.__init__(self , name , species = "Dog" )
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed:{self.breed}")