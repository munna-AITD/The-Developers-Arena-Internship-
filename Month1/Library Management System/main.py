from all_menus import *


def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            add_book_menu()
        elif choice == "2":
            view_books_menu()
        elif choice == "3":
            search_book_menu()
        elif choice == "4":
            issue_book_menu()
        elif choice == "5":
            return_book_menu()
        elif choice == "6":
            delete_book_menu()
        elif choice == "7":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
