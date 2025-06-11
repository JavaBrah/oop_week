from .animal import Animal

class Bird(Animal):
    list_of_birds = []
    
    @classmethod
    def add_to_list_of_birds(cls, bird):
        cls.list_of_birds.append(bird)

    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan
        self.add_to_list_of_birds(self)

    @property
    def wingspan(self):
        return self._wingspan
    
    @wingspan.setter
    def wingspan(self, new_wingspan):
        if new_wingspan:
            self._wingspan = new_wingspan
        else:
            raise ValueError("Wingspan not added")

    
