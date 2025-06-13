

class School:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.student = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("worng name")