import os
from student import Student

# Absolute path of this folder:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# students.txt inside Student_Management folder
FILE_NAME = os.path.join(BASE_DIR, "student.txt")


def add_student(student):
    with open(FILE_NAME, "a") as file:
        file.write(student.to_string())


def read_all_students():
    student = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                student.append(Student.from_string(line))
    except FileNotFoundError:
        pass
    return student


def write_all_students(student):
    with open(FILE_NAME, "w") as file:
        for student in student:
            file.write(student.to_string())
