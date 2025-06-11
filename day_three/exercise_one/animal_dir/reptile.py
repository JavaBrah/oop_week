from .animal import Animal

class Reptile(Animal):
    list_of_reptiles = []

    @classmethod
    def add_to_list_of_reptiles(cls, reptile):
        cls.list_of_reptiles.append(reptile)
    
    def __init__(self, name, species):
        super().__init__(name, species)
        self.add_to_list_of_reptiles(self)

    def bask_in_sun(self):
        print("sweat")


