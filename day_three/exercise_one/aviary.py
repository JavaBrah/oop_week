from animal_dir.bird import Bird

class Aviary():
    def __init__(self, birds= Bird.list_of_birds):
        self.birds = birds

    @property
    def birds(self):
        return self._birds
    
    @birds.setter
    def birds(self, list_of_birds):
        if isinstance(list_of_birds, list):
            self._birds = list_of_birds
        else:
            raise ValueError("Inputs bird objects in list form")