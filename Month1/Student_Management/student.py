class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def to_string(self):
        return f"{self.roll_no},{self.name},{self.marks}\n"

    @staticmethod
    def from_string(line):
        roll_no, name, marks = line.strip().split(",")
        return Student(roll_no, name, marks)
