def save_student(name, marks):
    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print(" No student records found")
            return

        print("\n Student List")
        for line in students:
            name, marks = line.strip().split(",")
            print(f"{name} - {marks}")

    except FileNotFoundError:
        print(" No student records file found")


def search_student():
    search_name = input("Enter student name to search: ").lower()
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                if search_name in name.lower():
                    print(f"🔍 Found: {name} - {marks}")
                    found = True

        if not found:
            print("❌ Student not found")

    except FileNotFoundError:
        print("⚠️ No student records file found")


def main():
    while True:
        print("\n--- Student Marks System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = input("Enter marks: ")
            save_student(name, marks)
            print("✅ Student record saved")

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("👋 Exiting program")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
