

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
        else:
            raise ValueError("Name was not added")
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, new_species):
        if new_species:
            self._species = new_species
        else:
            raise ValueError("Species not added")