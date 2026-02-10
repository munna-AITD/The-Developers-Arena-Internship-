from student import Student
from file_ops import add_student, read_all_students, write_all_students


def add_student_menu():
    roll_no = input("Enter roll number: ")
    student = read_all_students()
#Check for duplicate rollno
    for s in student:
        if s.roll_no==roll_no:
            print("rollno already exist, try another roll no")
            return
        
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    student = Student(roll_no, name, marks)
    add_student(student)
    print("✅ Student added successfully")


def view_students_menu():
    student = read_all_students()
    if not student:
        print("⚠️ No student records found")
        return

    print("\n📋 Student List")
    for s in student:
        print(f"{s.roll_no} | {s.name} | {s.marks}")


def search_student_menu():
    roll = input("Enter roll number to search: ")
    student = read_all_students()

    for s in student:
        if s.roll_no == roll:
            print(f"🔍 Found: {s.roll_no} | {s.name} | {s.marks}")
            return

    print("❌ Student not found")


def update_student_menu():
    roll = input("Enter roll number to update: ")
    student = read_all_students()

    for s in student:
        if s.roll_no == roll:
            new_marks = input("Enter new marks: ")
            s.marks = new_marks
            write_all_students(student)
            print("✅ Marks updated")
            return

    print("❌ Student not found")
#Delete student records-------------
def delete_student_menu():
    roll = input("Enter roll no to delete that student")
    student = read_all_students()

    for s in student:
        if s.roll_no == roll:
            student.remove(s)
            write_all_students(student)
            print("Student records deleted successfully")
            return
    print("Student not found")
        
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete student ")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student_menu()
        elif choice == "2":
            view_students_menu()
        elif choice == "3":
            search_student_menu()
        elif choice == "4":
            update_student_menu()
        elif choice == "5":
            delete_student_menu()
        elif choice == "6":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
