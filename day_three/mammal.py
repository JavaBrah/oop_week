from animal import Animal

class Mammal(Animal):
    
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        print("OW")

    