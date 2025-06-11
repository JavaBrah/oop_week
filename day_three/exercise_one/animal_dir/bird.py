from .animal import Animal

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    @property
    def wingspan(self):
        return self._wingspan
    
    @wingspan.setter
    def wingspan(self, new_wingspan):
        if new_wingspan:
            self._wingspan = new_wingspan
        else:
            raise ValueError("Wingspan not added")
