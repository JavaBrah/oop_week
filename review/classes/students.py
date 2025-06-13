import csv
# student.py
class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.school_id = school_id
    @classmethod
    def all_students(cls, file):
        students = []
        with open(file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row['age'] = int(row['age'])
                row['name'] = cls(**row)
                students.append(row["name"])
        return students

students = Student.all_students("./data/student.csv")
for s in students:
   
    print(type(s.age))