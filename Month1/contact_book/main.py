from contacts import format_contact, parse_contact
from file_ops import add_contact_to_file, read_contacts

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contact = format_contact(name, phone)
    add_contact_to_file(contact)
    print("Contact added successfully")

def view_contacts():
    contacts = read_contacts()
    if not contacts:
        print("No contacts found")
        return
    
    print("\n contact list")
    for line in contacts:
        name, phone = parse_contact(line)
        print(f"{name} - {phone}")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    contacts = read_contacts
    found = False

    for line in contacts:
        name, phone = parse_contact(line)
        if search_name in name.lower():
            print(f"Found: {name} - {phone}")
            found = True

    if not found:
        print("Contact not found")

def main():
    while True:
        print("\n--Contact Book ----")
        print("1. Add contact")
        print("2. view contacts ")
        print("3. search contacts")
        print("4. Exit")

        choice = input("Choose an option  ")
        if choice =="1":
            add_contact()
        elif choice =="2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodby!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    main()
        