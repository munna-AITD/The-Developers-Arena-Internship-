from book import Book
from file_ops import *


def add_book_menu():
    book_id = input("Enter Book ID: ")
    books = read_all_books()

    for b in books:
        if b.book_id == book_id:
            print("❌ Book ID already exists")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = Book(book_id, title, author)
    add_book(book)
    print("✅ Book added successfully")


def view_books_menu():
    books = read_all_books()
    if not books:
        print("📂 No books available")
        return

    for b in books:
        print(f"{b.book_id} | {b.title} | {b.author} | {b.status}")


def search_book_menu():
    key = input("Enter Book ID or Title: ")
    books = read_all_books()

    for b in books:
        if b.book_id == key or b.title.lower() == key.lower():
            print(f"Found: {b.book_id} | {b.title} | {b.author} | {b.status}")
            return

    print("❌ Book not found")


def issue_book_menu():
    book_id = input("Enter Book ID to issue: ")
    books = read_all_books()

    for b in books:
        if b.book_id == book_id:
            if b.status == "Issued":
                print("❌ Book already issued")
                return
            b.status = "Issued"
            write_all_books(books)
            print("✅ Book issued successfully")
            return

    print("❌ Book not found")


def return_book_menu():
    book_id = input("Enter Book ID to return: ")
    books = read_all_books()

    for b in books:
        if b.book_id == book_id:
            b.status = "Available"
            write_all_books(books)
            print("✅ Book returned successfully")
            return

    print("❌ Book not found")


def delete_book_menu():
    book_id = input("Enter Book ID to delete: ")
    books = read_all_books()

    for b in books:
        if b.book_id == book_id:
            books.remove(b)
            write_all_books(books)
            print("🗑️ Book deleted")
            return

    print("❌ Book not found")
