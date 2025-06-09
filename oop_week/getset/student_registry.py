

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name) >= 3 and name.isalpha():
            self._name = name
        else:
            raise ValueError("Name must be a string with more than 3 alphabetic characters.")   
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age: int):
        if isinstance(age, int) and 11 < int(age) < 18:
            self._age = age
        

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade: str):
        grade_number = "".join(c for c in grade if c.isdigit())
        if 9 <= int(grade_number) <= 12 and grade.endswith("th"):
            self._grade = grade
  
    
    @property
    def __str__(self):
        return f"Student: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def years_advanced(self, grade):
        if self.grade != grade:
            return f"{self.name} has advanced to the {grade}"

    def study(self, subject):
        return f"{self.name} is studying {subject}"
    
Student1 = Student("yep", 14, "12th")
