from animal_dir.reptile import Reptile

class ReptileEnclosure():
    list_of_enclosures = []

    @classmethod
    def add_to_list_of_enclosures(cls, enclosure):
        cls.list_of_enclosures.append(enclosure)


    def __init__(self, reptiles):
        self.reptiles = reptiles
        self.add_to_list_of_enclosures(self)

        

    @property
    def reptiles(self):
        return self._reptiles
    
    @reptiles.setter
    def reptiles(self, list_of_reptiles):
        if isinstance(list_of_reptiles, list):
            self._reptiles = list_of_reptiles
        else:
            raise ValueError("Reptiles must be in list type")
        
reptile1 = Reptile("Jerry", "lizard")
reptile2 = Reptile("Steve", "snake")
# print(Reptile.list_of_reptiles)

rep = ReptileEnclosure(Reptile.list_of_reptiles)
reptile3 = Reptile("Doug", "big lizard")
rep1 = ReptileEnclosure([reptile3])
print([r.name for r in rep.reptiles])
print([rep.name for rep in rep1.reptiles])