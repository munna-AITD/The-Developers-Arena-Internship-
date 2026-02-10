import csv
import os

file_path = r'C:/Users/Lenovo/Desktop/project_arena/Complete Python Personal Finance Manager/data/expenses.csv'
backup_path = r'C:/Users/Lenovo/Desktop/project_arena/Complete Python Personal Finance Manager/data/expenses_backup.csv'


def save_expenses(expenses, filename=file_path):
    file_exists = os.path.exists(filename)

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

        for expense in expenses:
            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.description
            ])


def load_expenses(filename=file_path):
    expenses = []

    if not os.path.exists(filename):
        return expenses

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)

    return expenses


def backup_data():
    if os.path.exists(file_path):
        with open(file_path, 'r') as src, open(backup_path, 'w') as dest:
            dest.write(src.read())
        print("✅ Backup created successfully")
    else:
        print("❌ No data file found")