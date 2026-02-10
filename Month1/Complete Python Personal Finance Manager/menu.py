from expense import Expense
from file_manager import save_expenses, load_expenses, backup_data
from utils import get_amount, get_date
from reports import category_summary, monthly_report

expenses_list = []


def show_menu():
    print("""
MAIN MENU
1. Add New Expense
2. View All Expenses
3. View Category-wise Summary
4. Generate Monthly Report
5. Search Expenses
6. Backup Data
7. Exit
""")


def add_expense():
    amount = get_amount()
    category = input("Enter category: ")
    date = get_date()
    description = input("Enter description: ")

    exp = Expense(amount, category, date, description)
    expenses_list.append(exp)
    save_expenses(expenses_list)
    print("✅ Expense added")


def view_expenses():
    data = load_expenses()
    for exp in data:
        print(exp)


def search_expense():
    key = input("Enter keyword: ").lower()
    data = load_expenses()

    for exp in data:
        if key in exp['Category'].lower() or key in exp['Description'].lower():
            print(exp)
        else:
            print("Key not found matching")


def handle_choice(choice):
    data = load_expenses()

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        category_summary(data)
    elif choice == '4':
        month = input("Enter month (YYYY-MM): ")
        monthly_report(data, month)
    elif choice == '5':
        search_expense()
    elif choice == '6':
        backup_data()
    elif choice == '7':
        print("👋 Exiting...")
        exit()
    else:
        print("❌ Invalid choice")
