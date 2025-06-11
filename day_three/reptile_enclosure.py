from animal_dir.reptile import Reptile

class ReptileEnclosure():
    def __init__(self, reptiles):
        self.reptiles = reptiles

    @property
    def reptiles(self):
        return self._reptiles
    
    @reptiles.setter
    def reptiles(self, list_of_reptiles):
        if isinstance(list_of_reptiles, list):
            self._reptiles = list_of_reptiles
        else:
            raise ValueError("Reptiles must be in list type")