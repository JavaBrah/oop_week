import pytest 
from student_registry import Student

def test_student_initialization():
    student = Student("Alice", 13, "12th")
    assert student.name == "Alice"
    assert student.age == 13
    assert student.grade == "12th"

def test_student_name_setter():
    student = Student("Alice", 13, "12th")
    student.name = "Alex"
    assert student.name == "Alex"

def test_student_age_setter():
    student = Student("Alice", 13, "12th")
    student.age = 14
    assert student.age == 14

def test_student_grade_setter():
    student = Student("Alice", 13, "12th")
    student.grade = "10th"
    assert student.grade == "10th"

def test_invalid_name_setter():
    student = Student("Alice", 13, "12th")
    try:
        student.name = 123  # Should raise ValueError
    except ValueError:
        pass  # This is expected
    assert student.name == "Alice"

def test_invalid_age_setter():
    student = Student("Alice", 13, "12th")
    student.age = "invalid"
    assert student.age == 13

def test_invalid_grade_setter():
    student = Student("Alice", 17, "12th")
    student.grade = "13th"
    assert student.grade == "12th"
